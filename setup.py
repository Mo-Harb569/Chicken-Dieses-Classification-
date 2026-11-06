import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-Dieses-Classification-"
AUTHOR_USER_NAME = "Mo-Harb569"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "mhmad32harp@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/Mo-Harb569/Chicken-Dieses-Classification-",
    project_urls={
        "Bug Tracker": "https://github.com/Mo-Harb569/Chicken-Dieses-Classification-/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)