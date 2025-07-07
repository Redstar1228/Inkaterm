from setuptools import setup, find_packages

setup(
    name='inkaterm',
    version='1.0.1',
    description='convert PNG images to ASCII colored art',
    author='redstar1228',
    author_email='aliakbarzarei41@gmail.com',
    packages=find_packages(),
    install_requires=[
        'termcolor',
        'pillow',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
