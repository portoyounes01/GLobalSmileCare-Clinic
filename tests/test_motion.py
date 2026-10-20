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
        self.assertIn("transform: translateY(-5px)", css)
        self.assertIn("filter: saturate(1.04)", css)

    def test_hero_has_a_visible_entry_motion_and_load_fallback(self):
        script = (ROOT / "script.js").read_text()
        css = (ROOT / "premium.css").read_text()
        self.assertIn(".hero-copy', '.hero-visual", script)
        self.assertIn(".motion-ready .hero-copy { animation: hero-enter 850ms", css)
        self.assertIn("@media (prefers-reduced-motion: no-preference) {\n  .motion-ready .hero-copy", css)
        self.assertIn("@keyframes hero-enter", css)
        self.assertIn("motion-replay", script)
        self.assertNotIn("if (!prefersReducedMotion) {\n  const replayMotion", script)
        self.assertIn(".motion-preview .hero-copy", css)
        self.assertIn("animation: hero-enter 850ms", css)
        self.assertIn(".motion-preview .reveal-item.is-visible", css)
        self.assertIn("enableScrollMotion();", script)

    def test_scroll_reveals_are_staggered_as_targets_enter_the_view(self):
        script = (ROOT / "script.js").read_text()
        css = (ROOT / "premium.css").read_text()
        self.assertIn("main > section:not(.hero)", script)
        self.assertIn(".sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)", script)
        self.assertIn("Math.min(index, 5) * 180", script)
        self.assertIn("transition: opacity 900ms", css)


if __name__ == "__main__":
    unittest.main()
