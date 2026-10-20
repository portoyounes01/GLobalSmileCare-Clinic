from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "dist"


class ServiceDetailPageTests(unittest.TestCase):
    def test_services_learn_more_opens_checkup_detail(self):
        services = (ROOT / "services.html").read_text()
        self.assertIn('href="service-details.html"', services)

    def test_detail_page_includes_complete_care_sections_and_footer(self):
        detail = ROOT / "service-details.html"
        self.assertTrue(detail.is_file(), "service detail route should exist")
        html = detail.read_text()
        for heading in ("Why Regular Checkups Matter", "What To Expect", "Frequently Asked Questions", "Join Our Newsletter"):
            self.assertIn(heading, html)

    def test_detail_page_has_checkup_heading_and_local_hero_photo(self):
        detail = ROOT / "service-details.html"
        self.assertTrue(detail.is_file(), "service detail route should exist")
        html = detail.read_text()
        self.assertIn("Teeth Cleaning &amp; Dental Checkups", html)
        self.assertTrue((ROOT / "assets" / "service-detail-hero.jpg").is_file())
        css = (ROOT / "styles.css").read_text()
        self.assertIn("assets/service-detail-hero.jpg", css)


if __name__ == "__main__":
    unittest.main()
