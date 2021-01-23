import setuptools
from os.path import join, abspath, dirname

PACKAGE_NAME = "fama_api"

# VERSION INFO
about = {}
with open(join(abspath(dirname(__file__)), PACKAGE_NAME, '__version__.py')) as f:
    exec(f.read(), about)

# README
with open("README.md", "r", encoding="utf-8") as fh:
    __long_description__ = fh.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=about['__title__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    long_description=__long_description__,
    long_description_content_type="text/markdown",
    url=f"https://github.com/fama/{PACKAGE_NAME}",
    packages=setuptools.find_packages(),
    dependency_links=[
        "git+git://github.com/FAMA-News/fama-models@main",
        "git+git://github.com/FAMA-News/fama-processing@main"
    ],
    install_requires=[
        "fastapi==0.63.0",
        "uvicorn==0.13.3",
        "pydantic==1.7.3"
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
