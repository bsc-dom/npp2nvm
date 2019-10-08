from setuptools import setup

setup(name='npP2NVM',
      version="0.1",
      install_requires=[
          "pynvm",
      ],
      description='NumPy Persistence to Non-Volatile Memory',
      packages=["npp2nvm"],
      )
