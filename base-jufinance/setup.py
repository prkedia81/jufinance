from setuptools import setup, find_packages

VERSION = "0.0.11"
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
        "async-generator",
        "attrs",
        "beautifulsoup4",
        "bs4",
        "certifi",
        "charset-normalizer",
        "exceptiongroup",
        "h11",
        "idna",
        "lxml",
        "numpy",
        "outcome",
        "pandas",
        "PySocks",
        "python-dateutil",
        "pytz",
        "requests",
        "selenium",
        "six",
        "sniffio",
        "sortedcontainers",
        "soupsieve",
        "tomli",
        "trio",
        "trio-websocket",
        "tzdata",
        "urllib3",
        "wsproto",
    ],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python", "first package"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        # "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
