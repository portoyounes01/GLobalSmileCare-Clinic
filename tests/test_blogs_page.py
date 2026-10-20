from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "dist"


class BlogsPageTests(unittest.TestCase):
    def test_blogs_page_has_article_listing_and_local_figma_images(self):
        page = ROOT / "blogs.html"
        self.assertTrue(page.is_file(), "Blogs route should exist")
        html = page.read_text()
        for text in ("Dental Care Insights", "Latest Articles", "Read, learn, and smile",
                     "What to Expect During Your First Dental Visit", "When to See a Dentist About Tooth Pain"):
            self.assertIn(text, html)
        for asset in ("article-child-figma.png", "article-toothache-figma.png", "article-braces-figma.png"):
            self.assertTrue((ROOT / "assets" / asset).is_file(), asset)
            self.assertIn(asset, html)

    def test_blogs_navigation_targets_dedicated_page(self):
        for name in ("index.html", "services.html", "service-details.html", "about.html", "doctors.html"):
            html = (ROOT / name).read_text()
            self.assertIn('href="blogs.html"', html, name)
        home = (ROOT / "index.html").read_text()
        self.assertIn('href="blogs.html">Browse Articles', home)
        html = (ROOT / "blogs.html").read_text()
        self.assertIn('aria-current="page"', html)


if __name__ == "__main__":
    unittest.main()
