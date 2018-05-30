# nl2bash_server
Submodule of the nl2bash project at https://github.com/oisindoherty/nl2bash

Run the server from the top project directory with:
- `pip3 install pipenv` (if you don't have pipenv)
- `pipenv run python manage.py migrate` (if the db.sqlite3 isn't setup)
- `pipenv run python -m nl2bash_server.add_data_from_scraper test_pages/ScrapedPages` (this might take a few minutes)
- `pipenv run python manage.py runserver`

To publicly show the website, you can run the following instead after adding your domain name to ALLOWED_HOSTS in nl2bash_server/settings.py:
- `pipenv run python manage.py runserver 0.0.0.0:12321` (you can change the port from 12321)

Check the user manual for help using the tester interface. The user manual can be found at
https://github.com/oisindoherty/nl2bash/blob/master/nl2bash_user_manual.pdf

Refer to: https://docs.djangoproject.com/en/2.0/intro/tutorial01/#the-development-server
for more information about running the development server.

When finished verifying pairs, use the following to save the validations to all.cm and all.nl:
- `pipenv run python -m nl2bash_server.save_data`
