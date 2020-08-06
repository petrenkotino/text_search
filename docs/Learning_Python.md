# Project: "Learn Python enough to complete Schibsted's homework assingment"

## First things first: How does one do Python?
### What is the fuss about this Python aynaway
Google: python
  
  *Interpreted language; Supports multiple paradigms; Dynamically typed...*

  Python 2, Python 3... Seems like there was a major change, and a lot of noise when the change happened.

  - Check if Python3 (is that the one I should be using?) is installed on my machine? (It was, I'm going for Python3, sounds newer than Python2 anyway)
    - Probably a good idea to install Python with `homebrew`. Probably even better to use a version manager like `pyenv`

## Project structure
How does a Python project look like
  - Python projects appear to be pretty simple in their structure actually. Not much fluff.
  - Where do we keep dependency versions? ~~`requirements.txt`~~
    - Can I/Should Imake a distinction between dev/prod dependencies? 
  - Packages and modules? `__init__.py`seems to be a thing of the past. Since I'm using Python 3.8, I can skip that
  - Do I need `setup.py`? It seems like it is more relevant if one wants to distribute a module.

*Oh wait!* Python seems to install dependencies globally, not per project! Shit f$ck, how did I miss that... 

_...some time later..._

Ah ok, seems like I can solve this with having virtual env per project... Of course, there are multiple ways of doing this (duh :P). 
Using `pipenv` reminds me of using `npm`, I'll go with that, and skip learning how to use `venv`, `virtualenv` and whtever else is out there.

Dependencies can be managed via `pipenv`, and it can handle dev and prod dependencies also, which is nice! I can get rid of `requirements.txt`, yay!

## Testing
  - Is ther esomething built in, or do I need a lib? --> Going with `pytest`. There is a built in `unittest` lib, but `pytest` feels a bit better for now (According to the internet pytest is a no boilerplate alternative to unittest. I like no boilerplate).
    - Pytest runs OK without explicit config for where test files, or what makes a test if I follow some conventions. That is good enough for this project.
    - Pytest fixtures mehanism is a powerfull way that leverages DI for eg. setup/teardown of tests. Don't forget that fixtures can be scoped (function - default, package, module, class)! 
    - How to run a single test? --> `% pytest -k <substr>` to search for substrings, `% pytest -m <marker>` to run tests with specific markers. These 2 should do the trick for now. Markers are cool!
    - How to skip tests? --> There seems to be a marker @skip.
    - Pytest parametarized testing looks awesome!
  - Mocking/stubbing in case I need it --> Seems like there is a `mock` library. Apparently it is included in the standard lib, so I shouldn't have to install it (is this true?)
  - Test coverage --> There is a pytest-cov module. Not going to use it for this example, but might be good to look into

  - TOX?

## Logging

Going with good ol' `print('stuff')` in case I need logging for this project.

## Linting

Pylint? Not enough time to experiment with this now, although would be fun to learn how to do this.

## Code styles/formatting

Trying to follow this: https://www.python.org/dev/peps/pep-0008/

## Debugging

Debugging (when running tests) in VSCode worked like a charm!

## Errors/Exceptions

This seems to be pretty straightforward and similar to other languages.

I like the `with` statement. Seems kinda intuitive to use, and saves a few lines of code, although one might argue that it makes things less explicit.

## Other
- Ensuring things work cross platform (cross OS) - seems like Python's OS module handles that for us

### Collections
Working with collections in Python seems intuitive, biggest difference is list comprehensions, which at first seemed weird, but the first time I wrote one, it felt kinda natural.


## TODO
Code formatting (prettier?)
Code conventions
Error handling: Built in errors?