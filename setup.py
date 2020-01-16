from setuptools import setup, find_packages


requirements = ['requests']

setup(
    name="GaisTokenizer",
    version="0.10",
    description="GaisTokenizer Service Python API",
    author="GAIS LAB & aqweteddy@github",
    url="",
    license="MIT",
    include_package_data=True,
    packages=find_packages(include=["src"]),
    install_requires=requirements
    # scripts=["scripts/test.py"],
)