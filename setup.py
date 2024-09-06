from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="geco3",
    version="v0.1.0-alpha",
    author="Tymoteusz Strojny",
    author_email="tymek.strojny@gmail.com",
    description="A flexible data generation and corruption system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/T-Strojny/Python3_GeCo_data_generator_corurptor",
    packages=find_packages(where="geco3"),
    classifiers=[
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
    install_requires=[],
)