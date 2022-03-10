# API Softdesk
[OpenClassRoom mission for project_10](https://openclassrooms.com/fr/paths/322/projects/838/assignment)

## Install:
  Install virtual env [here](https://virtualenvwrapper.readthedocs.io/en/latest/)
  ```
  - mkvirtualenv project_10
  - workon project_10
  - pip install -r requirements.txt
  - python manage.py runserver 8001
  ```
  
## Download API Schema:
  - Run server with ```python manage.py runserver 8001 ```
  - Open your browser then type http://localhost:8001/schema

## Development utilities:
  Run autoformat.sh in order to format code with blake, flake8 and isort
  
  To generate a new flake8 report, please use this command:
  ```flake8 --format=html --htmldir=flake-report```
