from setuptools import setup

n = "featuresetenrichment"

setup(
    name=n,
    version="0.1.0",
    python_requires=">=3.6",
    install_requires=(
        "julia",
        "pandas",
    ),
    packages=(n,),
)
