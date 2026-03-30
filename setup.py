from setuptools import setup, find_packages
import pathlib
import re

# Version aus __init__.py ohne Import und ohne exec() extrahieren
version_file = (
    pathlib.Path(__file__).parent
    / "src"
    / "eteaching"
    / "plone"
    / "openbadges"
    / "__init__.py"
)

with open(version_file, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(
    r'__version__\s*=\s*[^\'"]+[\'"]',
    content
)

if not match:
    raise RuntimeError("Unable to find __version__ in __init__.py")

package_version = match.group(1)

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="eteaching.plone.openbadges",
    version=package_version,
    description="Open Badge integration for Plone 6.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPL-2.0-only",
    python_requires=">=3.10",
    author="Author Name",
    author_email="a.email@mail.de",
    url="https://test.de",
    keywords=["CMS", "Plone", "Python"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Addon",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    install_requires=[
        "Products.CMFPlone",
        "plone.api",
        "z3c.jbot",
    ],
    extras_require={
        "test": [
            "horse-with-no-namespace",
            "plone.app.testing",
            "plone.classicui",
            "plone.restapi[test]",
            "pytest",
            "pytest-cov",
            "pytest-plone>=1.0.0a2",
        ],
        "release": [
            "zest.releaser[recommended]",
            "zestreleaser.towncrier",
            "zest.pocompile",
        ],
    },
    entry_points={
        "plone.autoinclude.plugin": [
            "target = plone",
        ],
    },
)