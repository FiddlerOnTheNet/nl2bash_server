# nl2bash_server
Submodule of the nl2bash project at https://github.com/oisindoherty/nl2bash

Run the server from the top project directory with:

    bash runserver.sh

Upon hitting enter, this saves all validated pairs and places them into all.cm and all.nl in the root of this repository.

To publicly show the website, you can change the following in the script after adding your domain name to ALLOWED_HOSTS in nl2bash_server/settings.py:

    pipenv run python manage.py runserver 0.0.0.0(:port#)

Check the user manual for help using the tester interface. The user manual can be found at
https://github.com/oisindoherty/nl2bash/blob/master/nl2bash_user_manual.pdf

Refer to: https://docs.djangoproject.com/en/2.0/intro/tutorial01/#the-development-server
for more information about running the development server.
