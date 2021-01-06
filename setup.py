from os import listdir

from setuptools import setup

name = "sea"

directory_path = "{}/data/".format(name)

setup(
    name=name,
    version="0.1.0",
    python_requires=">=3.6",
    install_requires=(
        "julia"
        "pandas",
    ),
    packages=(name,),
    package_data={
        name: tuple(
            "{}{}".format(directory_path, name) for name in listdir(path=directory_path)
        )
    },
)
