# Pacman

This is a very simple pacman game implemented in Python. The goal of
this project is to teach students a bit about code quality.

Pacman is implemented in three versions:

* The `spaghetti/` folder contains a single file. Everything is in there. What a mess!
This is the kind of code we should avoid.

* The `refactored/` folder contains a more elegant version of the game. Functions are small
and tested, it's definitely easier to understand and maintain.

* The `oop/` folder contains an implementation of Pacman that makes use of some
cool features of OOP languages, like inheritance and polymorphism.

## Running the project

_You must have Python 3 installed (and not Python 2!)_

- Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
    - `pip install virtualenv`
- Create a virtual environment
    - `python -m virtualenv venv`
- Activate the virtual environment
    - `source venv/bin/activate`
- Install all the dependencies
    - `pip install -r requirements.txt`

To run the tests (+ coverage): `py.test --cov-report html --cov=refactored *tests.py`

To run pylint, `pylint *.py`.

## License

Creative Commons.

