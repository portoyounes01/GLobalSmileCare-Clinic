from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "dist"


class AboutPageTests(unittest.TestCase):
    def test_about_page_describes_the_real_clinic(self):
        html = (ROOT / "about.html").read_text()
        for text in ("Global Smile Care", "Antwerpen-Zuid", "Tandprotheses", "Woonzorgcentra", "Tolstraat 40"):
            self.assertIn(text.casefold(), html.casefold())

    def test_about_page_keeps_its_design_assets_and_styles(self):
        html = (ROOT / "about.html").read_text()
        self.assertIn('href="about.css"', html)
        self.assertIn('href="styles.css"', html)
        css = (ROOT / "about.css").read_text()
        self.assertIn("appointment-banner-figma.webp", css)
        self.assertTrue((ROOT / "assets" / "appointment-banner-figma.webp").is_file())

    def test_about_navigation_opens_dedicated_page(self):
        for name in ("index.html", "services.html", "service-details.html", "about.html"):
            html = (ROOT / name).read_text()
            self.assertIn('href="about.html">Onze praktijk</a>', html, name)

    def test_home_about_button_opens_dedicated_page(self):
        html = (ROOT / "index.html").read_text()
        self.assertIn('href="about.html">Onze praktijk ↗</a>', html)


if __name__ == "__main__":
    unittest.main()
