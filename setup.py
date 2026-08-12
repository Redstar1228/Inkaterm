from pathlib import Path
from setuptools import setup, find_packages

README = Path("README.md").read_text(encoding="utf-8")

setup(
    name = "inkaterm",
    version = "2.0.2",
    description = "Convert PNG images to ASCII colored art",
    author = "Redstar1228",
    author_email = "aliakbarzarei41@gmail.com",
    long_description = README,
    long_description_content_type = "text/markdown",
    packages = find_packages(include = ["inkaterm", "inkaterm.*"]),
    include_package_data = True,
    install_requires = [
        "pillow",
        "lz4"
    ],
    python_requires = ">= 3.8",
)