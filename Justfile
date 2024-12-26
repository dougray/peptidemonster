# Justfile for managing FastAPI Peptide Prices API

# Set the default shell to bash
set shell := ["bash", "-cu"]

# Command to install dependencies
install-deps:
    pip install -r requirements.txt

# Command to run the FastAPI application
run:
    uvicorn app.main:app --reload

# Command to run tests (if you have tests)
test:
    pytest

# Command to format code using black
format:
    black .

# Command to lint code using flake8
lint:
    flake8 .

# Command to check for security issues using bandit
security-check:
    bandit -r .

# Command to clean up __pycache__ and other temporary files
clean:
    find . -type d -name "__pycache__" -exec rm -r {} +
    find . -type f -name "*.pyc" -delete