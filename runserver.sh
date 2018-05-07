#!/bin/bash
pip install pipenv
pipenv run python manage.py migrate
pipenv run python -m nl2bash_server.add_data_from_scraper test_pages/ScrapedPages
pipenv run python manage.py runserver
