from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Python3_GeCo_data_generator_corurptor",
    version="v0.1.0-alpha",
    author="Tymoteusz Strojny",
    author_email="tymek.strojny@gmail.com",
    description="A flexible data generation and corruption system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/T-Strojny/Python3_GeCo_data_generator_corurptor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
    install_requires=[
        
    ],
    package_data={
        "Python3_GeCo_data_generator_corurptor": ["lookup-files/*.csv"],
    },
)