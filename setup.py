from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="ivep",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A collection of tools for analyzing protein interaction data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ivep",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ivep=ivep.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "pymol"
    ],
)
