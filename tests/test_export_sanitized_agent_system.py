import json

import export_sanitized_agent_system as e
from _fixtures import tok, _FILL2


class TestSanitize:
    def test_redacts_telegram_token(self):
        assert e.sanitize(tok("12345678:", 30)) == "[REDACTED_TELEGRAM_BOT_TOKEN]"

    def test_redacts_github_token(self):
        assert e.sanitize(tok("ghp_", 20)) == "[REDACTED_GITHUB_TOKEN]"

    def test_redacts_openai_key(self):
        assert e.sanitize(tok("sk-", 20)) == "[REDACTED_OPENAI_KEY]"

    def test_openrouter_key_is_caught_by_openai_rule_first(self):
        # The openai rule precedes the openrouter rule in SECRET_PATTERNS, so an
        # sk-or-v1- key is redacted (as OPENAI) before the openrouter rule runs.
        assert e.sanitize(tok("sk-or-v1-", 20)) == "[REDACTED_OPENAI_KEY]"

    def test_redacts_notion_and_secret(self):
        assert e.sanitize(tok("ntn_", 20)) == "[REDACTED_NOTION_TOKEN]"
        assert e.sanitize(tok("secret_", 20)) == "[REDACTED_SECRET]"

    def test_redacts_airtable_pat(self):
        assert e.sanitize(tok("pat", 10) + "." + _FILL2 * 10) == "[REDACTED_AIRTABLE_PAT]"

    def test_redacts_bearer_token_case_insensitive(self):
        assert e.sanitize("Authorization: bearer " + _FILL2 * 25) == "Authorization: Bearer [REDACTED]"

    def test_redacts_key_value_pairs(self):
        assert e.sanitize("api_key = supersecretvalue") == "api_key = [REDACTED]"
        assert e.sanitize("token: abc123def") == "token: [REDACTED]"
        assert e.sanitize("password=hunter2") == "password=[REDACTED]"

    def test_leaves_clean_text_untouched(self):
        text = "this is a normal sentence"
        assert e.sanitize(text) == text


class TestWrite:
    def test_writes_sanitized_content_and_creates_parents(self, tmp_path, monkeypatch):
        monkeypatch.setattr(e, "REPO", tmp_path)
        e.write("nested/dir/out.txt", tok("ghp_"))
        written = (tmp_path / "nested/dir/out.txt").read_text()
        assert written == "[REDACTED_GITHUB_TOKEN]"


class TestSafeRead:
    def test_reads_existing_file(self, tmp_path):
        f = tmp_path / "a.txt"
        f.write_text("hello")
        assert e.safe_read(f) == "hello"

    def test_returns_none_on_oserror(self, tmp_path):
        # Reading a directory raises IsADirectoryError (an OSError subclass).
        assert e.safe_read(tmp_path) is None


class TestCopyText:
    def test_copies_when_source_exists(self, tmp_path, monkeypatch):
        monkeypatch.setattr(e, "REPO", tmp_path)
        src = tmp_path / "src.txt"
        src.write_text("token: leaked_value")
        e.copy_text(src, "dest.txt")
        assert (tmp_path / "dest.txt").read_text() == "token: [REDACTED]"

    def test_noop_when_source_missing(self, tmp_path, monkeypatch):
        monkeypatch.setattr(e, "REPO", tmp_path)
        e.copy_text(tmp_path / "does_not_exist.txt", "dest.txt")
        assert not (tmp_path / "dest.txt").exists()


class TestRglobSafe:
    def test_collects_all_files(self, tmp_path):
        (tmp_path / "a.md").write_text("x")
        sub = tmp_path / "sub"
        sub.mkdir()
        (sub / "b.txt").write_text("y")
        results = e.rglob_safe(tmp_path)
        names = sorted(p.name for p in results)
        assert names == ["a.md", "b.txt"]

    def test_empty_dir_returns_empty(self, tmp_path):
        assert e.rglob_safe(tmp_path) == []


class TestMain:
    def test_removes_outputs_and_writes_registry(self, tmp_path, monkeypatch):
        repo = tmp_path / "repo"
        home = tmp_path / "home"
        repo.mkdir()
        home.mkdir()
        # Pre-existing outputs that main() must wipe.
        stale = repo / "agents" / "Old"
        stale.mkdir(parents=True)
        (stale / "junk.md").write_text("stale")
        monkeypatch.setattr(e, "REPO", repo)
        monkeypatch.setattr(e, "HOME", home)

        e.main()

        assert not (repo / "agents" / "Old").exists()
        registry = json.loads((repo / "agent-registry.json").read_text())
        assert registry["repo"] == "limitless-ai-team-os"
        assert {a["name"] for a in registry["agents"]} == set(e.AGENTS)
