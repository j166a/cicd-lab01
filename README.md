# CI/CD Lab 01 - Continuous Integration Pipeline

## Overview

This lab implements a basic Continuous Integration pipeline using GitHub Actions.

The workflow runs automatically on every push and pull request and validates the application through:

- Python setup
- Linting with Pylint
- Unit testing with Python's built-in `unittest`
- Docker image build
- Docker image verification

The goal is to automatically detect code quality, test, and build issues before changes progress further.

## Project Structure

```text
cicd-lab01/
├── app/
│   ├── hello.py
│   └── test_hello.py
├── .dockerignore
├── .gitignore
├── Dockerfile
└── README.md
```

The GitHub Actions workflow is defined in:

```text
.github/workflows/ci.yaml
```

## CI Pipeline

The workflow is triggered by:

```yaml
on: [push, pull_request]
```

Pipeline flow:

```text
Push / Pull Request
        |
        v
Checkout Code
        |
        v
Set Up Python
        |
        v
Install Pylint
        |
        v
Lint Application
        |
        v
Run Unit Tests
        |
        v
Build Docker Image
        |
        v
Verify Docker Image
        |
        v
Success
```

## Application

The lab uses a small Python application with a corresponding unit test.

```text
app/
├── hello.py
└── test_hello.py
```

The tests use Python's built-in `unittest` framework, so no application `requirements.txt` file is required.

## Linting

Pylint is installed during the workflow and used to check the application code.

The linting stage helps detect:

- Formatting issues
- Missing documentation
- Code quality problems

If linting fails, the workflow stops and reports the failure.

## Automated Testing

The workflow runs the unit tests with:

```bash
python -m unittest discover
```

This discovers and executes the tests inside the application directory.

If a test fails, the pipeline stops before progressing to the Docker build stage.

## Docker Build

The application is packaged using Docker.

```dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY app/ .

CMD ["python", "hello.py"]
```

The workflow builds the image with:

```bash
docker build -t hello-app .
```

The pipeline then verifies that the Docker image exists after the build completes.

## .dockerignore

The `.dockerignore` file prevents unnecessary files from being included in the Docker build context.

Typical exclusions include:

```text
.git
.github
__pycache__
*.pyc
README.md
```

This keeps the build context smaller and avoids copying files into the image that the application does not need.

## .gitignore

The `.gitignore` file prevents generated or local-only files from being committed to the repository.

Typical exclusions include:

```text
__pycache__/
*.pyc
.venv/
venv/
```

This keeps the repository clean and avoids committing temporary Python files or local environments.

## Issues Resolved

During implementation, the CI pipeline exposed several issues that needed to be corrected:

- `unittest` was initially treated as an external dependency even though it is part of the Python standard library.
- Pylint detected missing docstrings and formatting issues.
- Unit tests failed when the application behaviour did not match the expected test result.
- GitHub Actions workflow syntax was corrected for shell commands and Docker validation.
- Docker build paths were adjusted to match the project structure.

These failures demonstrated the value of CI by catching problems automatically before changes progressed further.

## What I Learnt

This lab reinforced:

- How GitHub Actions workflows are structured.
- How `push` and `pull_request` events trigger CI pipelines.
- How jobs and steps execute within a workflow.
- How linting can enforce code quality checks.
- How automated tests provide fast feedback.
- How pipeline failures help identify application issues.
- How Docker builds can be validated automatically.
- How `.dockerignore` reduces unnecessary Docker build context.
- How `.gitignore` keeps generated and local files out of version control.
- How CI provides a repeatable validation process for every code change.

## Result

The final GitHub Actions workflow successfully:

- Triggers automatically on pushes and pull requests.
- Runs linting.
- Runs unit tests.
- Builds the Docker image.
- Verifies the image build.
- Reports success only when all checks pass.