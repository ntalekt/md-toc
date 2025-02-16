import unittest
from md_toc.toc_generator import generate_toc


class TestTocGenerator(unittest.TestCase):
    def test_basic_toc(self):
        markdown = "# Title\n## Section 1\n### Subsection"
        expected_toc = "- [Section 1](#section-1)\n  - [Subsection](#subsection)"
        self.assertEqual(generate_toc(markdown), expected_toc)

    def test_max_level(self):
        markdown = "# Title\n## Section 1\n### Subsection"
        expected_toc = "- [Section 1](#section-1)"
        self.assertEqual(generate_toc(markdown, max_level=2), expected_toc)

    def test_indent(self):
        markdown = "# Title\n## Section 1\n### Subsection"
        expected_toc = (
            "    - [Section 1](#section-1)\n        - [Subsection](#subsection)"
        )
        self.assertEqual(generate_toc(markdown, indent=4), expected_toc)

    def test_special_characters(self):
        markdown = "# Title & More\n## Section 1: The Beginning"
        expected_toc = "- [Section 1: The Beginning](#section-1-the-beginning)"
        self.assertEqual(generate_toc(markdown, max_level=2), expected_toc)

    # Add more tests for edge cases and different Markdown structures.


if __name__ == "__main__":
    unittest.main()
