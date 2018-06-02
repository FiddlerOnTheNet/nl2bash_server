#!/bin/bash

# Taken from fullpipeline.sh in the parent repo.
pipenv run python manage.py migrate
pipenv run python -m nl2bash_server.add_data_from_scraper ./test_pages/ScrapedPages
((pipenv run python manage.py runserver) > server.output) &
PID=$!
read -p "Press enter to stop hosting the tester ui interface and save to all.cm/.nl."
kill $PID
pipenv run python -m nl2bash_server.save_data
touch all.cm
touch all.nl
