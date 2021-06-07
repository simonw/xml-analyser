from setuptools import setup
import os

VERSION = "1.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="xml-analyser",
    description="Analyse the structure of an arbitrary XML file",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/xml-analyser",
    project_urls={
        "Issues": "https://github.com/simonw/xml-analyser/issues",
        "CI": "https://github.com/simonw/xml-analyser/actions",
        "Changelog": "https://github.com/simonw/xml-analyser/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["xml_analyser"],
    entry_points="""
        [console_scripts]
        xml-analyser=xml_analyser.cli:main
    """,
    install_requires=[],
    extras_require={"test": ["pytest"]},
    tests_require=["xml-analyser[test]"],
)
