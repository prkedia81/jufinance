from setuptools import setup, find_packages

VERSION = "0.0.21"
DESCRIPTION = "Python Package to access Indian Stock market data."
LONG_DESCRIPTION = "Python Package to access Indian Stock market data. This is for educational purposes only."

# Setting up
setup(
    name="jufinance",
    version=VERSION,
    author="Prannay Kedia & Sparsh Gupta",
    author_email="<prannaykedia1@gmail.com>, <sparshgupta2407@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
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
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ],
)
