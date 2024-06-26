# WordWise Web App 🌎 📖

Welcome to the README for WordWise, a web application for language learning and vocabulary management.

## Table of Contents
* [Description](#description)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [Contact](#contact)
* [Testing](#testing)

## Description

WordWise is a Flask-based web application designed to help users learn and manage vocabulary in multiple languages. It allows users to translate words, view their meanings, and save them to a personal word bank for future reference.

## Features

* User authentication (signup, login, logout)
* Word translation to multiple target languages
* Display of translated words
* Personal word bank for saving and reviewing vocabulary
* Sorting and filtering functionality to break vocabulary into bitesize chunks
* Support for multiple languages

## Technologies Used

* Backend: Python, Flask
* Frontend: HTML, CSS, Javascript
* Database: PostgreSQL 
* External API: Vocabulary fetching API from deepl.com
    Please note: this API requires a free API Key, which you can set up directly on deepl.com. 

## Installation

To run WordWise locally, you'll need to install:

* Python 3.x
* Flask
* Other dependencies listed in the project's requirements.txt file. You can install these locally with the following command: pip install -r requirements.txt

Steps:

1. Clone the repository:
git clone https://github.com/olikelly00/wordwise-web-app.git
Copy2. Navigate to the project directory:
cd wordwise-web-app
Copy3. Install the required dependencies:
pip install -r requirements.txt


## Usage

1. Set up your database and update the connection details in the `database_connection.py` file.
2. Run the application:
python app.py
Copy3. Open a web browser and navigate to `http://localhost:5000`

## Project Structure

The WordWise Web App is organized as follows:

- `app.py`: Main application file containing route definitions and app configuration
- `lib/`: Directory containing helper modules and core functionality
- `logfile`: Log file for the application
- `Pipfile`: Pipenv file for managing project dependencies
- `readme.md`: Project documentation (this file)
- `requirements.txt`: List of Python package dependencies
- `seeds/`: Directory for database seed files
  - `database_connection.sql`
  - `seeds_words.sql`
- `static/`: Directory for static files
  - `css/`: CSS stylesheets
- `templates/`: Directory for HTML templates
  - `login.html`: Login page template
  - `signup.html`: Sign-up page template
  - `welcome.html`: Welcome page template
  - `word.html`: Word display page template
  - `wordbank.html`: Word bank page template
- `tests/`: Directory containing test files
  - `__init__.py`
  - `conftest.py`: Configuration file for pytest
  - `test_database_connection.py`
  - `test_user_repository.py`
  - `test_user.py`
  - `test_vocab_fetcher.py`
  - `test_word_repository.py`
  - `test_word.py`
- `wordwise_venv/`: Virtual environment directory


This structure separates concerns, with distinct directories for application logic, templates, static files, tests, and database operations. The use of a virtual environment (`wordwise_venv`) ensures consistent dependency management across different development environments.


## Testing

WordWise uses pytest for its testing framework. To run the tests, follow these steps:

1. Ensure you have installed all dependencies, including pytest, which is listed in the `requirements.txt` file.

2. From the root directory of the project, run the following command: pytest

This will discover and run all tests in the `tests/` directory.

3. For more verbose output, you can use:

4. To run tests from a specific file, use:pytest tests/test_file_name.py

Replace `test_file_name.py` with the name of the test file you want to run.

5. To run a specific test function, use:

pytest tests/test_file_name.py::test_function_name

6. If you want to see print statements and other output during test execution, use: pytest -sv (add multiple v's for more detailed error messaging)

