"""Checks the Steward V1 starter kit is complete, opt-ins default off, and nothing private slipped in."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STEPS = [
    "steps/01-wake-up.md",
    "steps/02-basic-communications.md",
    "steps/03-storage-and-cloud.md",
]


EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})")
PHONE = re.compile(r"\(?\b\d{3}\)?[-. ]\d{3}[-. ]\d{4}\b")
TOKEN = re.compile(r"\b(hf_|ghp_|gho_|github_pat_|sk-)[A-Za-z0-9_-]{8,}")


def text_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".bak" in path.name or "__pycache__" in path.parts:
            continue
        yield path


class KitTests(unittest.TestCase):
    def test_required_files(self):
        for rel in ["README.md", "OPT-IN-SETTINGS.md", "LICENSE", ".gitignore",
                    "templates/flare-email.conf", *STEPS]:
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_readme_links_steps(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for rel in STEPS:
            self.assertIn(rel, readme)

    def test_flare_email_default_off(self):
        conf = (ROOT / "templates/flare-email.conf").read_text(encoding="utf-8")
        self.assertIn("flare_email: off", conf)

    def test_gitignore_blocks_working_copies(self):
        self.assertIn("*.bak*", (ROOT / ".gitignore").read_text(encoding="utf-8"))

    def test_scrub(self):
        hits = []
        for path in text_files():
            for n, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                for m in EMAIL.finditer(line):
                    if m.group(1).lower() != "example.org":
                        hits.append(f"{path.relative_to(ROOT)}:{n} email")
                if PHONE.search(line):
                    hits.append(f"{path.relative_to(ROOT)}:{n} phone")
                if TOKEN.search(line):
                    hits.append(f"{path.relative_to(ROOT)}:{n} token")
        self.assertEqual(hits, [])

    def test_cloud_expansion_default(self):
        step3 = (ROOT / "steps/03-storage-and-cloud.md").read_text(encoding="utf-8")
        optin = (ROOT / "OPT-IN-SETTINGS.md").read_text(encoding="utf-8")
        kit = step3 + "\n" + optin
        low = kit.lower()
        self.assertIn("allotment", low)
        self.assertIn("expand", low)
        self.assertIn("contract", low)
        self.assertIn("offload", low)
        self.assertIn("off-limits", low)
        self.assertIn("cold", low)
        self.assertIn("never offload them, never back them up, and never open them", low)
        # The old suggested 1 GB starting cap is no longer the default.
        self.assertIsNone(re.search(r"\b1\s*GB\b", kit, re.I))
        self.assertNotIn("300 GB", kit)
        self.assertNotIn("a common start is 1 GB", low)
        self.assertNotIn("1 gb is a good start", low)
        self.assertNotIn("1 gb is a common start", low)


if __name__ == "__main__":
    unittest.main()
