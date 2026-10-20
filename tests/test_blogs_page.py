from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "dist"


class BlogsPageTests(unittest.TestCase):
    def test_blogs_page_has_dutch_articles_and_local_images(self):
        html = (ROOT / "blogs.html").read_text()
        for text in ("Tandzorg met aandacht", "Uit onze praktijk", "Wat gebeurt er tijdens een eerste tandartsbezoek?", "Wanneer gaat u met tandpijn naar de tandarts?"):
            self.assertIn(text, html)
        for asset in ("article-child-figma.webp", "article-toothache-figma.webp", "article-braces-figma.webp"):
            self.assertTrue((ROOT / "assets" / asset).is_file(), asset)
            self.assertIn(asset, html)

    def test_blogs_navigation_targets_dedicated_page(self):
        for name in ("index.html", "services.html", "service-details.html", "about.html", "doctors.html"):
            html = (ROOT / name).read_text()
            self.assertIn('href="blogs.html"', html, name)
        self.assertIn('aria-current="page"', (ROOT / "blogs.html").read_text())


if __name__ == "__main__":
    unittest.main()
