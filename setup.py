from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="currency_ch",
    version="0.0.1",
    description="Python library for currency exchange.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/calebyhan/currency",
    author="Caleb Han",
    author_email="calebhantech@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(
        where='src'
    ),
    package_dir={"":"src"},
    include_package_data=True
)