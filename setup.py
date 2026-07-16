from setuptools import setup, find_packages

setup(
    name = "inkaterm",
    version = "2.0.0",
    description = "Convert PNG images to ASCII colored art",
    author = "Redstar1228",
    author_email = "aliakbarzarei41@gmail.com",
    packages = find_packages(include = ["inkaterm", "inkaterm.*"]),
    include_package_data = True,
    install_requires = [
        "pillow",
        "lz4"
    ],
    python_requires = ">= 3.8",
)