#!/bin/bash
pip install pipenv
pipenv run python manage.py migrate
pipenv run python -m nl2bash_server.add_data_from_scraper
timeout 10 pipenv run python manage.py runserver
