# nl2bash_server
Submodule of the nl2bash project at https://github.com/oisindoherty/nl2bash

Run the server from the top project directory with:
- `pip install pipenv` (if you don't have pipenv)
- `pipenv run python manage.py migrate` (if the db.sqlite3 isn't setup)
- `pipenv run python -m nl2bash_server.add_data_from_scraper test_pages/ScrapedPages` (this might take a few minutes)
- `pipenv run python manage.py runserver`

This is compacted into a shell script, which can be run with:
- `sh runserver.sh` on linux (assumes pip refers to the package manager for python 3; modify the command/file to pip3 or whatever the command is if needed)

Refer to: https://docs.djangoproject.com/en/2.0/intro/tutorial01/#the-development-server
for more information about running the development server.
