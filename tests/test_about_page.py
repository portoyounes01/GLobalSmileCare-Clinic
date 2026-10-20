from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "dist"


class AboutPageTests(unittest.TestCase):
    def test_about_page_contains_all_figma_sections(self):
        page = ROOT / "about.html"
        self.assertTrue(page.is_file(), "About Us route should exist")
        html = page.read_text()
        for text in (
            "Raising The Standard Of Dental Care",
            "Smarter,",
            "Modern Dentistry",
            "Personalised Treatment",
            "Comfort-Focused Technology",
            "Meet Our Dental Team",
            "Don’t Wait Book",
            "Your Questions",
            "Our team is happy to help",
            "Join Our Newsletter",
        ):
            self.assertIn(text, html)

    def test_about_page_uses_project_figma_assets_and_isolated_styles(self):
        page = ROOT / "about.html"
        self.assertTrue(page.is_file(), "About Us route should exist")
        html = page.read_text()
        css = (ROOT / "about.css").read_text()
        for asset in (
            "doctor-1-figma.webp", "doctor-2-figma.webp", "doctor-3-figma.webp",
            "doctor-4-figma.webp", "appointment-banner-figma.webp",
        ):
            self.assertTrue((ROOT / "assets" / asset).is_file(), asset)
            self.assertIn(asset, html + css)
        self.assertIn('href="about.css"', html)
        self.assertIn('href="styles.css"', html)

    def test_about_navigation_opens_dedicated_page_from_every_site_page(self):
        for name in ("index.html", "services.html", "service-details.html", "about.html"):
            html = (ROOT / name).read_text()
            self.assertIn('href="about.html">About Us</a>', html, name)

    def test_home_about_button_does_not_scroll_to_another_section(self):
        html = (ROOT / "index.html").read_text()
        self.assertIn('<a class="button small" href="about.html">About Us ↗</a>', html)


if __name__ == "__main__":
    unittest.main()
