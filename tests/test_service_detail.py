from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "dist"


class ServiceDetailPageTests(unittest.TestCase):
    def test_services_learn_more_opens_checkup_detail(self):
        services = (ROOT / "services.html").read_text()
        self.assertIn('href="service-details.html"', services)

    def test_detail_page_includes_clinic_specific_information_and_booking(self):
        html = (ROOT / "service-details.html").read_text()
        for text in ("Waarom een controle belangrijk is", "Wat kunt u verwachten?", "Veelgestelde vragen", "Global Smile Care", "Gaatjes vullen"):
            self.assertIn(text, html)
        self.assertIn('https://agenda.clickdocdentist.be/short/2B4OaRgY5BLx6ZVG', html)

    def test_detail_page_has_local_hero_photo(self):
        html = (ROOT / "service-details.html").read_text()
        self.assertTrue((ROOT / "assets" / "service-detail-hero.webp").is_file())
        self.assertIn("assets/service-detail-hero.webp", (ROOT / "styles.css").read_text())


if __name__ == "__main__":
    unittest.main()
