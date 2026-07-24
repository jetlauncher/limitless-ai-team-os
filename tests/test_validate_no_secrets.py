import validate_no_secrets as v
from _fixtures import tok, _FILL2


class TestScanText:
    def test_detects_telegram_bot_token(self):
        assert "telegram bot token" in v.scan_text(tok("12345678:", 30))

    def test_detects_github_token(self):
        assert "github token" in v.scan_text(tok("ghp_", 20))

    def test_detects_openai_key(self):
        assert "openai key" in v.scan_text(tok("sk-", 20))

    def test_detects_openrouter_key(self):
        assert "openrouter key" in v.scan_text(tok("sk-or-v1-", 20))

    def test_detects_notion_token_ntn(self):
        assert "notion token" in v.scan_text(tok("ntn_", 20))

    def test_detects_notion_token_secret_prefix(self):
        assert "notion token" in v.scan_text(tok("secret_", 20))

    def test_detects_airtable_pat(self):
        assert "airtable pat" in v.scan_text(tok("pat", 10) + "." + _FILL2 * 10)

    def test_clean_text_returns_empty(self):
        assert v.scan_text("just some harmless text with no secrets") == []

    def test_short_token_not_matched(self):
        # Too few trailing characters to satisfy the {20,}/{30,} quantifiers.
        assert v.scan_text("sk-short") == []

    def test_multiple_hits_reported(self):
        text = tok("ghp_", 20) + " and " + tok("sk-", 20, _FILL2)
        hits = v.scan_text(text)
        assert "github token" in hits
        assert "openai key" in hits


class TestScanTree:
    def test_finds_secret_in_file(self, tmp_path):
        (tmp_path / "leaky.txt").write_text(tok("ghp_"))
        found = v.scan_tree(tmp_path)
        assert ("leaky.txt", "github token") in found

    def test_returns_relative_paths(self, tmp_path):
        sub = tmp_path / "nested"
        sub.mkdir()
        (sub / "cfg.yaml").write_text(tok("sk-", ch="Z"))
        found = v.scan_tree(tmp_path)
        assert found == [("nested/cfg.yaml", "openai key")]

    def test_ignores_git_directory(self, tmp_path):
        git_dir = tmp_path / ".git"
        git_dir.mkdir()
        (git_dir / "config").write_text(tok("ghp_"))
        assert v.scan_tree(tmp_path) == []

    def test_skips_validator_itself(self, tmp_path):
        (tmp_path / "validate_no_secrets.py").write_text(tok("sk-"))
        assert v.scan_tree(tmp_path) == []

    def test_clean_tree_returns_empty(self, tmp_path):
        (tmp_path / "a.txt").write_text("nothing here")
        (tmp_path / "b.md").write_text("# clean doc")
        assert v.scan_tree(tmp_path) == []


class TestMain:
    def test_returns_zero_when_clean(self, tmp_path, capsys):
        (tmp_path / "ok.txt").write_text("all good")
        assert v.main(tmp_path) == 0
        assert "No obvious secrets found." in capsys.readouterr().out

    def test_returns_one_when_secret_found(self, tmp_path, capsys):
        (tmp_path / "bad.txt").write_text(tok("sk-"))
        assert v.main(tmp_path) == 1
        out = capsys.readouterr().out
        assert "Potential secrets found:" in out
        assert "openai key" in out
