import re


def generate_toc(markdown_text, max_level=6, indent=2):
    lines = markdown_text.splitlines()
    toc_lines = []
    heading_pattern = re.compile(r"^(#+)\s+(.+)$")

    for line in lines:
        match = heading_pattern.match(line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            if level <= max_level:
                # Create a link-friendly slug (lowercase, hyphens instead of spaces, remove special characters)
                slug = title.lower().replace(" ", "-")
                slug = re.sub(r"[^a-z0-9-]", "", slug)

                # Format the TOC line
                toc_line = f"{' ' * indent * (level - 1)}- [{title}](#{slug})"
                toc_lines.append(toc_line)

    return "\n".join(toc_lines)
