from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "dist"


class DoctorsPageTests(unittest.TestCase):
    def test_team_page_uses_real_clinic_facts(self):
        html = (ROOT / "doctors.html").read_text()
        for text in ("Global Smile Care", "Nieuwe patiënten zijn welkom", "Antwerpen-Zuid", "Tolstraat 40", "info@globalsmilecare.be"):
            self.assertIn(text, html)
        self.assertIn('id="dentists-title"', html)
        self.assertIn('id="assistants-title"', html)
        self.assertIn('Portugese achtergrond', html)
        self.assertEqual(html.count('class="team-role-card"'), 2)
        self.assertNotIn('class="doctor-profile"', html)
        for placeholder in ("Arlene McCoy", "Robert Fox", "Implant Specialist", "Orthodontist"):
            self.assertNotIn(placeholder, html)

    def test_team_page_uses_its_styles_and_verified_online_booking(self):
        html = (ROOT / "doctors.html").read_text()
        self.assertIn('href="doctors.css"', html)
        self.assertIn('href="styles.css"', html)
        self.assertIn('https://agenda.clickdocdentist.be/short/2B4OaRgY5BLx6ZVG', html)

    def test_sitewide_team_links_open_dedicated_page(self):
        for name in ("index.html", "services.html", "service-details.html", "about.html"):
            html = (ROOT / name).read_text()
            self.assertIn('href="doctors.html">Ons team</a>', html, name)


if __name__ == "__main__":
    unittest.main()
