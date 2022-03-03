#! /bin/sh

autoflake --remove-all-unused-imports --remove-unused-variables --remove-duplicate-keys \
  --recursive --in-place .

isort .

flake8 --ignore E203,E501,W503 .
 
black --line-length=100 --exclude softdesk/api/migrations \
  softdesk \
  $@