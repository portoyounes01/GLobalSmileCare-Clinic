from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1] / "dist"


class MotionTests(unittest.TestCase):
    def test_motion_respects_reduced_motion_and_reveals_visible_content(self):
        script = (ROOT / "script.js").read_text()
        css = (ROOT / "premium.css").read_text()
        self.assertIn("prefers-reduced-motion: reduce", script)
        self.assertIn("IntersectionObserver", script)
        self.assertIn("unobserve", script)
        self.assertIn(".motion-ready .reveal-item.is-visible", css)
        self.assertRegex(css, r"@media\s*\(prefers-reduced-motion:\s*reduce\)[\s\S]*?\.reveal-item[^}]*transition:\s*none")

    def test_cards_have_gentle_hover_motion_only_for_hover_devices(self):
        css = (ROOT / "premium.css").read_text()
        self.assertIn("@media (hover: hover) and (prefers-reduced-motion: no-preference)", css)
        self.assertIn(".motion-card:hover", css)
        self.assertIn("transform: translateY(-3px)", css)


if __name__ == "__main__":
    unittest.main()
