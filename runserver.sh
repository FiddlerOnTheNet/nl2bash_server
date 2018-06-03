#!/bin/bash

# Taken from fullpipeline.sh in the parent repo.
pipenv install
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
echo Loading .verify files into database.
pipenv run python -m nl2bash_server.add_data_from_scraper ./test_pages/ScrapedPages
pipenv run python manage.py runserver
echo
echo Outputting all.cm and all.nl from database.
pipenv run python -m nl2bash_server.save_data
touch all.cm
touch all.nl
