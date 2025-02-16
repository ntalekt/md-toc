# tests/test_cli.py
import unittest
import subprocess
import os
import tempfile
import sys  # added sys import


class TestCli(unittest.TestCase):
    def test_basic_toc_generation(self):
        # Create a temporary Markdown file
        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".md"
        ) as tmpfile:
            tmpfile.write(
                "# Test Document\n<!-- TOC -->\n## Section 1\n### Subsection 1.1"
            )
            temp_filename = tmpfile.name

        # Run the CLI command (CORRECTED)
        result = subprocess.run(
            ["md-toc", temp_filename], capture_output=True, text=True
        )

        # Check the output
        self.assertEqual(result.returncode, 0)  # Check for successful execution

        # Read modified file
        with open(temp_filename, "r") as file:
            modified_content = file.read()
        # Assert that the TOC was inserted correctly
        self.assertIn("- [Section 1](#section-1)", modified_content)
        self.assertIn("  - [Subsection 1.1](#subsection-11)", modified_content)
        os.remove(temp_filename)

    def test_stdout_output(self):
        # Create a temporary Markdown file
        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".md"
        ) as tmpfile:
            tmpfile.write("# Test Document\n## Section 1\n### Subsection 1.1")
            temp_filename = tmpfile.name

        # Run the CLI command with --stdout (CORRECTED)
        result = subprocess.run(
            ["md-toc", temp_filename, "--stdout"], capture_output=True, text=True
        )

        # Check the output
        self.assertEqual(result.returncode, 0)
        self.assertIn("- [Section 1](#section-1)", result.stdout)
        self.assertIn("  - [Subsection 1.1](#subsection-11)", result.stdout)
        os.remove(temp_filename)

    # Add more tests for different options and edge cases (e.g., max_level, indent, file not found)


if __name__ == "__main__":
    unittest.main()
