# -*- coding: utf-8 -*-
"""Installer for the eteaching.plone.openbadges package."""

from setuptools import find_packages
from setuptools import setup

long_description = "\n\n".join(
    [
        open("README.md").read()
    ]
)

setup(
    name="eteaching.plone.openbadges",
    version="1.1.2",
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
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["eteaching", "eteaching.plone"],
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
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = eteaching.plone.openbadges.locales.update:update_locale
    """,
)