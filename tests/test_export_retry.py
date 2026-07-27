import json

import export_retry as r
from _fixtures import tok, _FILL2


class TestSanitize:
    def test_redacts_known_secret_shapes(self):
        assert r.sanitize(tok("ghp_")) == "[REDACTED_GITHUB_TOKEN]"
        assert r.sanitize(tok("ntn_", 20)) == "[REDACTED_NOTION_TOKEN]"
        assert r.sanitize(tok("pat", 10) + "." + _FILL2 * 10) == "[REDACTED_AIRTABLE_PAT]"

    def test_redacts_key_value_pairs(self):
        assert r.sanitize("api-key=abc123") == "api-key=[REDACTED]"
        assert r.sanitize("password: hunter2") == "password: [REDACTED]"

    def test_leaves_clean_text_untouched(self):
        assert r.sanitize("nothing secret here") == "nothing secret here"


class TestCatFile:
    def test_reads_existing_file(self, tmp_path):
        f = tmp_path / "a.txt"
        f.write_text("file contents")
        assert r.cat_file(f) == "file contents"

    def test_missing_file_returns_empty(self, tmp_path):
        assert r.cat_file(tmp_path / "missing.txt") == ""


class TestWrite:
    def test_writes_sanitized_content(self, tmp_path, monkeypatch):
        monkeypatch.setattr(r, "REPO", tmp_path)
        r.write("out/x.txt", "token=leaked")
        assert (tmp_path / "out/x.txt").read_text() == "token=[REDACTED]"


class TestCollect:
    def test_filters_by_extension(self, tmp_path):
        (tmp_path / "keep.md").write_text("a")
        (tmp_path / "skip.png").write_text("b")
        results = r.collect(tmp_path, r.exts, r.skip_names, r.skip_dirs)
        assert [f.name for f, _ in results] == ["keep.md"]

    def test_skips_named_and_dir_and_state_files(self, tmp_path):
        (tmp_path / "ACCESS-TOKENS.md").write_text("secret")
        (tmp_path / "state.json").write_text("{}")
        (tmp_path / "agent_state.json").write_text("{}")
        skipped_dir = tmp_path / "node_modules"
        skipped_dir.mkdir()
        (skipped_dir / "pkg.json").write_text("{}")
        (tmp_path / "good.md").write_text("ok")
        results = r.collect(tmp_path, r.exts, r.skip_names, r.skip_dirs)
        assert [f.name for f, _ in results] == ["good.md"]

    def test_skips_empty_files(self, tmp_path):
        (tmp_path / "empty.md").write_text("")
        assert r.collect(tmp_path, r.exts, r.skip_names, r.skip_dirs) == []

    def test_truncates_large_files(self, tmp_path):
        (tmp_path / "big.md").write_text("x" * 130000)
        results = r.collect(tmp_path, r.exts, r.skip_names, r.skip_dirs)
        _, txt = results[0]
        assert txt.endswith("[TRUNCATED FOR TEMPLATE REPO]\n")
        assert len(txt) < 130000

    def test_sanitizes_nothing_at_collect_time(self, tmp_path):
        # collect returns raw text; sanitization happens in write().
        secret = tok("ghp_")
        (tmp_path / "raw.md").write_text(secret)
        _, txt = r.collect(tmp_path, r.exts, r.skip_names, r.skip_dirs)[0]
        assert txt == secret


class TestMain:
    def test_writes_registry_and_clears_outputs(self, tmp_path, monkeypatch):
        repo = tmp_path / "repo"
        home = tmp_path / "home"
        repo.mkdir()
        home.mkdir()
        stale = repo / "configs" / "old"
        stale.mkdir(parents=True)
        (stale / "cfg.yaml").write_text("stale")
        monkeypatch.setattr(r, "REPO", repo)
        monkeypatch.setattr(r, "HOME", home)

        r.main()

        assert not (repo / "configs" / "old").exists()
        registry = json.loads((repo / "agent-registry.json").read_text())
        assert registry["repo"] == "limitless-ai-team-os"
        assert {a["name"] for a in registry["agents"]} == set(r.agents_map)
