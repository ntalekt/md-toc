import argparse
from .toc_generator import generate_toc


def main():
    parser = argparse.ArgumentParser(
        description="Generate a table of contents for a Markdown file."
    )
    parser.add_argument("input_file", help="Path to the input Markdown file.")
    parser.add_argument(
        "-o",
        "--output_file",
        help="Optional output file. If not specified, modifies the input file in place.",
        default=None,
    )
    parser.add_argument(
        "--max-level",
        type=int,
        default=6,
        help="Maximum heading level to include (default: 6).",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="Indentation level in spaces (default: 2).",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Output TOC to stdout instead of modifying the file.",
    )
    parser.add_argument(
        "--toc-marker",
        default="<!-- TOC -->",
        help="Marker in the file where the TOC should be inserted.",
    )

    args = parser.parse_args()

    try:
        with open(args.input_file, "r", encoding="utf-8") as f:
            markdown_text = f.read()

        toc = generate_toc(markdown_text, args.max_level, args.indent)

        if args.stdout:
            print(toc)
        else:
            if args.output_file:
                output_file = args.output_file
            else:
                output_file = args.input_file

            if args.toc_marker in markdown_text:
                updated_markdown = markdown_text.replace(args.toc_marker, toc)
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(updated_markdown)
                print(f"TOC inserted into {output_file}")
            else:
                print(
                    "TOC marker not found. No changes made to the file.",
                    file=sys.stderr,
                )

    except FileNotFoundError:
        print(f"Error: File not found: {args.input_file}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
