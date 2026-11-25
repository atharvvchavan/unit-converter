# Unit Converter

![CI/CD](https://github.com/atharvvchavan/unit-converter/actions/workflows/ci.yml/badge.svg)

A small Flask app that converts length, weight and temperature. I built it to practise CI/CD with GitHub Actions.

## The pipeline
1. **Lint** with flake8
2. **Test** with pytest on Python 3.11 and 3.12
3. **Build** the Docker image and smoke-test the running container
4. **Publish** the image to GitHub Container Registry (only on pushes to main)

## What I learned
- Separating logic (converter.py) from the web layer (app.py) so it is easy to test
- Parametrized tests with pytest
- Linting with flake8
- A GitHub Actions matrix, pip caching and job dependencies
- A smoke test of a running container
- Running a container as a non-root user
- Stamping a Docker image with its commit ID using a build argument
- The pull request workflow

## Run the tests
    pip install -r requirements-dev.txt
    flake8 .
    pytest -v

## Run with Docker
    docker build -t unit-converter .
    docker run -d -p 5050:5000 unit-converter
    open http://localhost:5050