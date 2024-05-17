"""" Setup """
from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="tn_timeular",
    version="0.1.0",
    description="Track your time with the Timeular cube and Timenote",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marsop/timenote-timeular",
    author="Alberto Gregorio",
    author_email="me@albertogregorio.com",
    license="MIT",
    packages=["tn_timeular"],
    install_requires=[
        "bleak",
        "recordclass",
        "appdirs",
        "requests",
        "PyYAML",
        "tenacity",
        "yamale",
    ],
    entry_points={
        "console_scripts": ["tn-timeular=tn_timeular:main"],
    },
)
