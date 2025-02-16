# md-toc: Markdown Table of Contents Generator

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Stargazers](https://img.shields.io/github/stars/ntalekt/md-toc?style=flat)](https://github.com/ntalekt/md-toc/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/ntalekt/md-toc?style=flat)](https://github.com/ntalekt/md-toc/commits/master)
[![Build Status](https://github.com/ntalekt/md-toc/actions/workflows/python-app.yml/badge.svg)](https://github.com/ntalekt/md-toc/actions)

`md-toc` is a simple command-line tool that generates a table of contents (TOC) for Markdown files. It can insert the TOC directly into your Markdown file or output it to the console.

## Features

*   Generates a nested, linked TOC from Markdown headings.
*   Inserts the TOC at a designated marker (default: `<!-- TOC -->`).
*   Outputs the TOC to the console if no marker is found or with the `--stdout` flag.
*   Controls the maximum heading level included (`--max-level`).
*   Customizes indentation (`--indent`).
*   Handles special characters and Markdown formatting in headings.

## Installation

```bash
git clone https://github.com/<your-username>/md-toc.git
cd md-toc
python setup.py install
```

## Usage

**Basic Usage (Insert TOC):**
```bash
md-toc input.md
```
This will search for <!-- TOC --> in input.md and replace it with the generated TOC. If the marker isn't found, no changes will be made to the file.

**Output to Console:**
```bash
md-toc input.md --stdout
```
This will print the generated TOC to the console without modifying the file.

**Specify Maximum Heading Level:**
```bash
md-toc input.md --max-level 3
```
This will include only headings up to H3 in the TOC.

**Specify custom Indentation:**
```bash
md-toc input.md --indent 4
```
This will use 4 spaces for indentation instead of the default 2.

**Specify output file:**
```bash
md-toc input.md -o output.md
```
This will create a new file output.md with the TOC inserted

**Help:**
```bash
md-toc --help
```

## Example
**Input Markdown (input.md):**
```markdown
# My Document

<!-- TOC -->

## Section 1

### Subsection 1.1

## Section 2

### Subsection 2.1

#### Sub-subsection 2.1.1
```

**Command:**
```bash
md-toc input.md
```

**Output Markdown (input.md - after running the command):**
```markdown
# My Document

<!-- TOC -->
- [Section 1](#section-1)
  - [Subsection 1.1](#subsection-11)
- [Section 2](#section-2)
  - [Subsection 2.1](#subsection-21)
    - [Sub-subsection 2.1.1](#sub-subsection-211)

## Section 1

### Subsection 1.1

## Section 2

### Subsection 2.1

#### Sub-subsection 2.1.1
```

## Testing
The project uses the unittest module for testing. To run the tests, navigate to the project's root directory (where setup.py is located) in your terminal and run:
```bash
python -m unittest discover tests
```

This command will automatically discover and run all test files (starting with test_) within the tests directory. Alternatively, you can run a specific test file:
```bash
python -m unittest tests/test_cli.py
python -m unittest tests/test_toc_generator.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Support

For issues or questions, please [open an issue](https://github.com/ntalekt/md-toc/issues)