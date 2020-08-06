from setuptools import setup, find_packages

with open('README.md') as f:
  readme = f.read()

setup(
    name='Text Search Magic',
    version="0.1",
    packages=find_packages(exclude=('tests', 'testfiles', 'docs')),
    author='Konstatin Petrenko',
    long_description=readme,
    description='A thing that can be used to search for text in text files',
)