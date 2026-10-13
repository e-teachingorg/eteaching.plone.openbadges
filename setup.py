# -*- coding: utf-8 -*-

from pathlib import Path
import re

from setuptools import find_namespace_packages
from setuptools import setup


long_description = Path("README.md").read_text(encoding="utf-8")

init_py = Path(
    "src/eteaching/plone/openbadges/__init__.py"
).read_text(encoding="utf-8")

match = re.search(
    r'^__version__ = ["\']([^"\']+)["\']',
    init_py,
    re.MULTILINE,
)

version = match.group(1)

setup(
    name="eteaching.plone.openbadges",
    version=version,
    description="Open Badge integration for Plone 6.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    keywords="CMS Plone Python",
    author="Markus Schmidt",
    author_email="m.schmidt@iwm-tuebingen.de",
    url="https://github.com/e-teachingorg/eteaching.plone.openbadges",
    project_urls={
        "Homepage": "https://github.com/e-teachingorg/eteaching.plone.openbadges",
        "PyPI": "https://pypi.org/project/eteaching.plone.openbadges",
        "Source": "https://github.com/e-teachingorg/eteaching.plone.openbadges",
        "Tracker": "https://github.com/e-teachingorg/eteaching.plone.openbadges/issues",
        "Documentation": "https://github.com/e-teachingorg/eteaching.plone.openbadges",
        "ChangeLog": "https://github.com/e-teachingorg/eteaching.plone.openbadges/blob/main/CHANGELOG.md",
    },
    license="GPL-2.0-only",
    packages=find_namespace_packages(
        "src",
        exclude=["ez_setup"],
    ),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
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
    entry_points="""
    [plone.autoinclude.plugin]
    target = plone
    """,
)
