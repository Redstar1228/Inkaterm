from setuptools import setup, find_packages

setup(
    name='inkaterm',
    version='1.2.0',
    description='Convert PNG images to ASCII colored art',
    author='redstar1228',
    author_email='aliakbarzarei41@gmail.com',
    packages=find_packages(include=["inkaterm", "inkaterm.*"]),
    include_package_data=True,
    package_data={
        "inkaterm": ["db/*.json"],
    },
    install_requires=[
        'termcolor',
        'pillow',
    ],
    python_requires='>=3.6',
)
