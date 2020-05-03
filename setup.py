from setuptools import setup, find_packages


requirements = ['requests']

setup(
    name="gaisTokenizer",
    version="0.2",
    description="GaisTokenizer Service Python API",
    author="GAIS LAB & aqweteddy@github",
    url="",
    license="MIT",
    include_package_data=True,
    packages=find_packages(include=["gaisTokenizer"]),
    install_requires=requirements
)