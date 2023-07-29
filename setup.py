from setuptools import find_packages, setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="event_schema_profcomff",
    version="2023.07.29.1",
    author="Semyon Grigoriev",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/profcomff/event-schema",
    packages=find_packages(),
    install_requires=["pydantic", "setuptools"],
    classifiers=[
        "Programming Language :: Python :: 3.11",
    ],
)
