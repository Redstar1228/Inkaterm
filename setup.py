from setuptools import setup, find_packages

setup(
    name='inkaterm',
    version='1.0.0',
    description='Render PPM images in colored terminal output',
    author='redstar1228',
    author_email='aliakbarzarei41@gmail.com',
    packages=find_packages(),
    install_requires=[
        'termcolor',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
