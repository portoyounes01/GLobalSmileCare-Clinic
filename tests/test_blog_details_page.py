from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "dist"


class BlogDetailsPageTests(unittest.TestCase):
    def test_blog_details_route_uses_site_styles_and_page_script(self):
        page = ROOT / "blog-details.html"
        self.assertTrue(page.is_file(), "Blog detail route should exist")
        html = page.read_text()
        self.assertIn('href="blog-details.css"', html)
        self.assertIn('src="blog-details.js"', html)
        self.assertIn('id="article-title"', html)
        self.assertIn('id="article-content"', html)

    def test_each_blog_preview_has_a_full_article_link(self):
        html = (ROOT / "blogs.html").read_text()
        for slug in ("first-visit", "tooth-pain", "braces-care"):
            self.assertIn(f'blog-details.html?article={slug}', html)

    def test_detail_script_supports_each_listed_article_and_local_photos(self):
        script = ROOT / "blog-details.js"
        self.assertTrue(script.is_file(), "Blog detail content script should exist")
        source = script.read_text()
        for slug in ("first-visit", "tooth-pain", "braces-care"):
            self.assertIn(slug, source)
        for photo in ("article-child-figma.webp", "article-toothache-figma.webp", "article-braces-figma.webp"):
            self.assertTrue((ROOT / "assets" / photo).is_file(), photo)
            self.assertIn(photo, source)


if __name__ == "__main__":
    unittest.main()
