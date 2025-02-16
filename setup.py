from setuptools import setup, find_packages

setup(
    name="md-toc",
    version="0.1.0",  # Use semantic versioning
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "md-toc = md_toc.cli:main",  # This makes 'md-toc' executable
        ],
    },
    install_requires=[],  # Add any dependencies here (if needed)
    author="ntalekt",
    author_email="ntalekt@users.noreply.github.com",
    description="A Markdown table of contents generator.",
    long_description=open(
        "README.md"
    ).read(),  # Use the README for the long description
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="markdown toc table-of-contents",
    url="https://github.com/ntalekt/md-toc",  # Replace with your repo URL
    classifiers=[  # See: https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
    ],
)
