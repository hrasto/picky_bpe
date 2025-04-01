import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="picky_bpe",
    version="0.0.1",
    author="Rastislav Hronsky",
    author_email="hronskyr@gmail.com",
    description='Fork of https://github.com/pchizhov/picky_bpe that wraps the code as a python package',
    url='https://github.com/pchizhov/picky_bpe',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[],
)
