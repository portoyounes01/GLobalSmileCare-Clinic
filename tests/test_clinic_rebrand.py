from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "dist"
BOOKING_URL = "https://agenda.clickdocdentist.be/short/2B4OaRgY5BLx6ZVG"


class ClinicRebrandTests(unittest.TestCase):
    def test_all_pages_use_the_clinic_identity_and_correct_locale(self):
        pages = sorted(ROOT.glob("*.html"))
        self.assertEqual(len(pages), 9)
        for page in pages:
            html = page.read_text()
            with self.subTest(page=page.name):
                language = {"en.html": "en", "pt.html": "pt"}.get(page.name, "nl")
                self.assertIn(f'<html lang="{language}">', html)
                self.assertIn("Global Smile Care", html)
                self.assertNotIn("Smile Dental Care", html)

    def test_clinic_contact_details_and_booking_are_real(self):
        home = (ROOT / "index.html").read_text()
        for value in (
            "Tolstraat 40", "2000 Antwerpen", "03 216 03 08",
            "info@globalsmilecare.be", BOOKING_URL,
        ):
            self.assertIn(value, home)
        self.assertNotIn("47800 Stanford", home)
        self.assertNotIn("+21 283 588982", home)

    def test_official_logo_is_used_across_pages(self):
        logo = ROOT / "assets" / "global-smile-care-logo.webp"
        self.assertTrue(logo.is_file())
        for page in ROOT.glob("*.html"):
            self.assertIn("global-smile-care-logo.webp", page.read_text(), page.name)

    def test_unverified_staff_and_services_are_not_present(self):
        combined = "\n".join(page.read_text() for page in ROOT.glob("*.html"))
        for placeholder in ("Arlene McCoy", "Xiofik Hasan", "Dental Implants", "Braces &amp; Aligners"):
            self.assertNotIn(placeholder, combined)


if __name__ == "__main__":
    unittest.main()
