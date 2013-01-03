from setuptools import setup, find_packages
from pantera import __version__


with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n') if (line and not line.startswith('--'))
    ]


setup(name="pantera",
      version=__version__,
      packages=find_packages(),
      description="tool to add some chaos on tsuru",
      author="timeredbull",
      author_email="timeredbull@corp.globo.com",
      install_requires=install_requires)
