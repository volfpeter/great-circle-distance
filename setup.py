import re
from codecs import open
from os import path
from setuptools import setup

# Get the long description from the README file.
with open(path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
    readme = f.read()

# Get version from the main project file.
with open(path.join(path.abspath(path.dirname(__file__)), "great_circle_distance.py"), encoding="utf-8") as f:
    match = re.search('__version__ = "(.*?)"', f.read())
    version = match.group(1) if match else "0.0.0"

# Requirements.
requirements = []

setup(
    name="great-circle-distance",
    version=version,
    description="Simple great circle distance calculation package.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/volfpeter/great-circle-distance",
    author="Peter Volf",
    author_email="do.volfp@gmail.com",
    license="MIT",
    classifiers=[],
    keywords="great-circle-distance distance sphere sheroid",
    py_modules=["great_circle_distance"],
    python_requires=">=3.7",
    install_requires=requirements,
)
