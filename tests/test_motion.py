from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1] / "dist"


class MotionTests(unittest.TestCase):
    def test_motion_respects_reduced_motion_and_reveals_visible_content(self):
        script = (ROOT / "script.js").read_text()
        css = (ROOT / "premium.css").read_text()
        self.assertIn("prefers-reduced-motion: reduce", script)
        self.assertIn("addEventListener('scroll', schedule", script)
        self.assertIn("window.innerHeight * 0.48", script)
        self.assertIn("requestAnimationFrame(updateScrollReveals)", script)
        self.assertIn(".motion-ready .reveal-item { will-change: opacity, transform; }", css)
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
        self.assertIn("enableScrollMotion();", script)

    def test_scroll_reveals_are_staggered_as_targets_enter_the_view(self):
        script = (ROOT / "script.js").read_text()
        css = (ROOT / "premium.css").read_text()
        self.assertIn(".faq-list details", script)
        self.assertIn("const revealOrderByGroup = new Map()", script)
        self.assertIn("Math.min(groupOrder, 3));", script)
        self.assertIn("Number(element.dataset.revealOrder || 0) * 48", script)
        self.assertIn("rect.top - staggerPixels", script)
        self.assertIn("window.addEventListener('resize', schedule", script)
        self.assertIn(".motion-ready .reveal-item", css)
        self.assertNotIn("clip-path: inset(100% 0 0)", css)

    def test_all_inner_pages_have_scroll_motion_targets(self):
        script = (ROOT / "script.js").read_text()
        for selector in (
            ".about-story", ".result-card", ".doctor-profile", ".doctor-directory-grid",
            ".blog-grid", ".article-content p", ".article-sidebar", ".article-help",
            ".service-detail-card", ".services-promo", ".detail-benefit-grid .value-card"
        ):
            with self.subTest(selector=selector):
                self.assertIn(selector, script)


if __name__ == "__main__":
    unittest.main()
