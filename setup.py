from setuptools import setup

name = "FeatureSetEnrichment"

setup(
    name=name,
    version="0.1.0",
    python_requires=">=3.6",
    install_requires=(
        "julia",
        "pandas",
    ),
    packages=(name,),
)
