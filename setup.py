import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="template-python",
    version="0.0.1",
    author="Aakash Hemadri",
    author_email="aakashhemadri123@gmail.com",
    description="A template python package",
    long_description="# A simple setup. - template-python",
    long_description_content_type="text/markdown",
    url="https://github.com/aakashhemadri/template-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)