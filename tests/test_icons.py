from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1] / "dist"


class IconTests(unittest.TestCase):
    def test_contact_cards_use_matching_vector_icons(self):
        for page_name in ("index.html", "doctors.html"):
            html = (ROOT / page_name).read_text()
            with self.subTest(page=page_name):
                for icon in ("map-pin", "phone", "mail"):
                    self.assertRegex(html, rf'class="contact-icon {icon}"[^>]*>\s*<svg')

    def test_dental_services_use_specific_icons_instead_of_decorative_characters(self):
        html = "\n".join((ROOT / name).read_text() for name in ("index.html", "services.html", "service-details.html", "doctors.html", "about.html"))
        self.assertNotRegex(html, r'class="(?:clinic-value-icon|clinic-service-icon)[^"]*">\s*[⌕✦◉＋]')
        for icon in ("checkup", "whitening", "denture", "filling", "care"):
            with self.subTest(icon=icon):
                self.assertRegex(html, rf'class="[^"]*icon-{icon}[^"]*"[^>]*>\s*<svg')

    def test_service_tabs_change_the_matching_icon(self):
        script = (ROOT / "script.js").read_text()
        for service, icon in (("checkups", "checkup"), ("whitening", "whitening"), ("dentures", "denture"), ("fillings", "filling")):
            self.assertIn(f"{service}: '{icon}'", script)
        self.assertIn("serviceIcon.querySelector('use')?.setAttribute('href'", script)


if __name__ == "__main__":
    unittest.main()
