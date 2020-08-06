# Text search

Solution for the Software Engineering (Python) challange for ACME.

## Prerequisite
- Python3 needs to be installed on your machine. You can download the binary for your OS from [here](https://www.python.org/downloads/)
- This project utilizes [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) for packaging/managing virtual envs.

## Running the app
1. cd to the project's root where `Pipfile` is located.
2. run `% pipenv install` in your shell.
3. run `% pipenv python -m run.py <path to a folder containing text files>` in your shell. (There is a folder `testfiles/` with some test files with random text in there already)

## Running the tests

1. Make sure all dependencies are installed (It will be if you run step 2 from `Runing the app` ☝️).
2. run `% pipenv run pytest` in your shell.

## Other files
- For the [Solution walkthrough](./docs/Solution_walkthrough.md)
- For reading on what I though about when I was learning Python (warning for uncensored content) [Learning Python](./docs/Learning_Python.md)