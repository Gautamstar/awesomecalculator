import setuptools
import os
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Cecil21899", # Replace with your own username
    version= "1.0.0",    #pypi-AgENdGVzdC5weXBpLm9yZwIkZmRmODgzNDYtMGEyNS00NTA2LTg0N2EtZmY1YjM0ZGJjNDIzAAIqWzMsImIxOWRjYWZhLThiNTEtNDUxNC1hZjlkLTBkZGMzNDk3MjdlNCJdAAAGINirtyV9A_w_p4a02EzunRWd2BDgOPACEsTJSKJUkqyH
    author="Daniel Edreira",
    author_email="dedreira@github.com",
    description="An awesome calculator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gautamstar/awesomecalculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)