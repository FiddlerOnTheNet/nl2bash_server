# Cleans the database, removing all entries.

import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nl2bash_server.settings")
django.setup()

from nl2bash_server_app.models import CommandPair, EnglishDescription, \
    BashCommand, Verification

def clean_all():
    """ Remove all entries from the database. """
    CommandPair.objects.all().delete()
    EnglishDescription.objects.all().delete()
    BashCommand.objects.all().delete()
    Verification.objects.all().delete()

# Uncomment to reset database
clean_all()
