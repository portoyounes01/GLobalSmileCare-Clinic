from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1] / "dist"


def contrast_ratio(first, second):
    def luminance(color):
        channels = [int(color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
        channels = [channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4 for channel in channels]
        return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]

    low, high = sorted((luminance(first), luminance(second)))
    return (high + 0.05) / (low + 0.05)


class MobileReadabilityTests(unittest.TestCase):
    def test_about_title_keeps_a_space_when_phone_layout_hides_the_break(self):
        html = (ROOT / "about.html").read_text()
        self.assertIn("Global Smile Care<br> uw tandarts", html)

    def test_treatment_tabs_wrap_and_keep_the_booking_link_on_phone(self):
        css = (ROOT / "premium.css").read_text()
        self.assertRegex(css, r"@media\s*\(max-width:\s*600px\)[\s\S]*?\.service-tabs\s*\{[^}]*display:\s*grid")
        self.assertRegex(css, r"@media\s*\(max-width:\s*600px\)[\s\S]*?\.service-tabs\s+a\s*\{[^}]*display:\s*inline-flex")
        self.assertIn(".service-tabs .pill { background: #e7f1eb; color: var(--clinic-forest); }", css)
        self.assertIn(".service-tabs .pill { display: inline-flex;", css)

    def test_mobile_small_copy_is_large_enough_to_read(self):
        doctors_css = (ROOT / "doctors.css").read_text()
        about_css = (ROOT / "about.css").read_text()
        self.assertIn(".doctors-page .doctor-caption h2{font-size:13px}", doctors_css)
        self.assertIn(".doctors-page .doctor-caption p{font-size:11px}", doctors_css)
        self.assertIn(".about-page .doctor-caption p{font-size:12px}", about_css)

    def test_home_cta_heading_stays_white_over_the_photo(self):
        css = (ROOT / "premium.css").read_text()
        self.assertRegex(css, r"\.cta\s+h2\s*\{[^}]*color:\s*#fff")

    def test_muted_text_and_brand_accent_meet_wcag_aa_on_clinic_surfaces(self):
        css = (ROOT / "premium.css").read_text()
        colors = dict(re.findall(r"(--[a-z-]+):\s*(#[0-9a-fA-F]{6})", css.split("}", 1)[0]))
        for foreground in ("--muted", "--clinic-forest"):
            for background in ("--clinic-paper", "--clinic-sage"):
                with self.subTest(foreground=foreground, background=background):
                    self.assertGreaterEqual(contrast_ratio(colors[foreground], colors[background]), 4.5)


if __name__ == "__main__":
    unittest.main()
