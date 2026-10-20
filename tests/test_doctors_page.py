from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "dist"


class DoctorsPageTests(unittest.TestCase):
    def test_doctors_page_contains_design_sections_and_six_profiles(self):
        page = ROOT / "doctors.html"
        self.assertTrue(page.is_file(), "Doctors route should exist")
        html = page.read_text()
        for text in (
            "Thoughtful Dental Care",
            "Expert dental care you can trust.",
            "Your Question",
            "Get in Touch",
            "Book Appointment",
            "Join Our Newsletter",
        ):
            self.assertIn(text, html)
        self.assertEqual(html.count('class="doctor-profile"'), 6)

    def test_doctors_page_uses_local_portraits_and_styles(self):
        page = ROOT / "doctors.html"
        self.assertTrue(page.is_file(), "Doctors route should exist")
        html = page.read_text()
        self.assertIn('href="doctors.css"', html)
        self.assertIn('href="styles.css"', html)
        for asset in ("doctor-1-figma.png", "doctor-2-figma.png", "doctor-3-figma.png",
                      "doctor-4-figma.png", "doctor-5-figma.png", "doctor-6-figma.jpg"):
            self.assertTrue((ROOT / "assets" / asset).is_file(), asset)
            self.assertIn(asset, html)

    def test_sitewide_doctors_links_open_doctors_page(self):
        for name in ("index.html", "services.html", "service-details.html", "about.html"):
            html = (ROOT / name).read_text()
            self.assertIn('href="doctors.html">Doctors</a>', html, name)


if __name__ == "__main__":
    unittest.main()
