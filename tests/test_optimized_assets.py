from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1] / "dist"


class OptimizedAssetTests(unittest.TestCase):
    def test_site_references_local_webp_images_without_png_or_jpeg(self):
        references = set()
        for page in ROOT.glob("*.html"):
            references.update(re.findall(r"assets/([\w.-]+\.(?:png|jpe?g|webp))", page.read_text(), re.I))
        for style in ROOT.glob("*.css"):
            references.update(re.findall(r"assets/([\w.-]+\.(?:png|jpe?g|webp))", style.read_text(), re.I))
        for script in ROOT.glob("*.js"):
            references.update(re.findall(r"assets/([\w.-]+\.(?:png|jpe?g|webp))", script.read_text(), re.I))
        self.assertTrue(references, "Site should use local image assets")
        self.assertTrue(all(name.lower().endswith(".webp") for name in references), sorted(references))
        for name in references:
            self.assertTrue((ROOT / "assets" / name).is_file(), name)

    def test_referenced_images_fit_a_reasonable_transfer_budget(self):
        references = set()
        for page in ROOT.glob("*.html"):
            references.update(re.findall(r"assets/([\w.-]+\.(?:png|jpe?g|webp))", page.read_text(), re.I))
        for style in ROOT.glob("*.css"):
            references.update(re.findall(r"assets/([\w.-]+\.(?:png|jpe?g|webp))", style.read_text(), re.I))
        for script in ROOT.glob("*.js"):
            references.update(re.findall(r"assets/([\w.-]+\.(?:png|jpe?g|webp))", script.read_text(), re.I))
        total_bytes = sum((ROOT / "assets" / name).stat().st_size for name in references)
        self.assertLess(total_bytes, 5_000_000, f"Referenced raster assets total {total_bytes:,} bytes")
        self.assertLess((ROOT / "assets" / "service-detail-hero.webp").stat().st_size, 500_000)


if __name__ == "__main__":
    unittest.main()
