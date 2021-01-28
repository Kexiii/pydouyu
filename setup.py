import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydouyu",
    version="0.0.6",
    author="kexiii",
    author_email="kexiii@163.com",
    description="Python implementation of douyu TV API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kexiii/pydouyu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
