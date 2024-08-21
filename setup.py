from setuptools import setup, find_packages

VERSION = "0.1.0"
DESCRIPTION = "Python Package to access Indian Stock market data."
LONG_DESCRIPTION = "Python Package to access Indian Stock market data. This is for educational purposes only."
GITHUB_URL = "https://github.com/prkedia81/jufinance"

# Setting up
setup(
    name="jufinance",
    version=VERSION,
    author="Prannay Kedia & Sparsh Gupta",
    author_email="prannaykedia1@gmail.com, sparshgupta2407@gmail.com",
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    packages=find_packages(),
    include_package_data=True,  # This ensures package data is included
    package_data={
        'jufinance': ['scrapers/links.json'],  # Add the path to links.json
    },
    install_requires=[
        "beautifulsoup4",
        "bs4",
        "pandas",
        "requests",
        "selenium",
    ],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python", "finance", "stock market"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
    license="MIT",
)
