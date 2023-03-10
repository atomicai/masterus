LINE_WIDTH=129
NAME := $(shell python setup.py --name)
UNAME := $(shell uname -s)
ISORT_FLAGS=--line-width=${LINE_WIDTH} --profile black
FLAKE_FLAGS=--remove-unused-variables --ignore-init-module-imports --recursive
# "" is for multi-lang strings (comments, logs), '' is for everything else.
BLACK_FLAGS=--skip-string-normalization --line-length=${LINE_WIDTH}
PYTEST_FLAGS=-p no:warnings
export FLASK_APP=masterus.tdk.rise

install:
	pip install -e '.[all]'

setup-pre-commit:
	pip install -q pre-commit
	pre-commit install
  	# To check whole pipeline.
	pre-commit run --all-files

format:
	isort ${ISORT_FLAGS} --check-only --diff ${NAME} masterus test
	black ${BLACK_FLAGS} --check --diff ${NAME} masterus test
	autoflake ${FLAKE_FLAGS} --in-place ${NAME} masterus test

format-fix:
	isort ${ISORT_FLAGS} ${NAME} masterus test
	black ${BLACK_FLAGS} ${NAME} masterus test
	autoflake ${FLAKE_FLAGS} ${NAME} masterus test

run:
	flask run --host=0.0.0.0 --port=2023

test:
	pytest test ${PYTEST_FLAGS} --testmon --suppress-no-test-exit-code

test-all:
	pytest test ${PYTEST_FLAGS}

clean:
	rm -rf .ipynb_checkpoints
	rm -rf **/.ipynb_checkpoints
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf downloads
	rm -rf wandb
	find . -name ".DS_Store" -print -delete
	rm -rf .cache
	pyclean .
