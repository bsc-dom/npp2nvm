from setuptools import setup

long_description = open("README.md").read()

setup(
    name='npP2NVM',
    version="0.2",
    install_requires=[
        "pynvm",
    ],
    author="Alex Barcelo",
    author_email="alex.barcelo@bsc.es",
    description='NumPy Persistence to Non-Volatile Memory',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["npp2nvm"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
    url="https://github.com/bsc-dom/npp2nvm",
    keywords="pynvm nvm persistence numpy",
)
