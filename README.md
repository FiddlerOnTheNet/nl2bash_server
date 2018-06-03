# nl2bash_server
Submodule of the nl2bash project at https://github.com/oisindoherty/nl2bash

To use this submodule: clone this submodule, cd into its root directory, replace the .verify files in test_pages/ScrapedPages with your
own if needed (a test set of .verify files is already in there), run this command:

    bash runserver.sh

Upon hitting CTRL-C, the server will safely exit and save all validated pairs, placing them into all.cm and all.nl in the root of this repository.
Note: the server will display a 'None' when it the tester has verified all the input files/pairs.

To publicly show the website, you can change the following in the script after adding your domain name to ALLOWED_HOSTS in nl2bash_server/settings.py:

    pipenv run python manage.py runserver 0.0.0.0(:port#)

Check the user manual for help using the tester interface. The user manual can be found at
https://github.com/oisindoherty/nl2bash/blob/master/nl2bash_user_manual.pdf

Refer to: https://docs.djangoproject.com/en/2.0/intro/tutorial01/#the-development-server
for more information about running the development server.
