# Simple Library

Example integration of PonyORM and FastAPI.

## Setup project

* Use `pipenv` to create virtualenv:
  ```bash
  pipenv --python 3.10
  pipenv shell
  pipenv install --dev
  ```
* Init database:
  ```bash
  make init
  ```

## Run app

Turn on pipenv shell and run:
  ```bash
  make run
  ```

Navigate to [http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/) to check API endpoints definitions.
