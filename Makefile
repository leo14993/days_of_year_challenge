# Variables
GIT_CURRENT_BRANCH := ${shell git symbolic-ref --short HEAD}
SRC_DIR := ./

setup_dev:
	@echo "---- Upgrading PIP ----"
	@pip install --upgrade pip
	@echo ""
	@echo ""
	@echo "---- Installing DEV Python dependencies ----"
	@pip install -r requirements-dev.txt


clean:
	@echo "---- Cleaning up .pyc files ----"
	@find . -name '*.pyc' -delete
	@rm -rf `find . -type d -name "__pycache__"`
	@rm -rf `find . -type d -name ".pytest_cache"`
	@rm -rf `find . -type d -name "htmlcov"`
	@echo "---- Cleaned ----"

coverage:
	@echo "---- Running tests coverage ----"
	@PYTHONPATH=$(BASE_DIR) pytest --cov=$(SRC_DIR)
	@coverage-badge > coverage.svg

