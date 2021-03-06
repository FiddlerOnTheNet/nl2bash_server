# Python script that adds data
# Format: From ScrapedPages - top line is the English command description,
# subsequent lines are bash commands suggested to match that English
# description.
# This script takes a directory of those files, then creates CommandPair
# entries in the database for them.

# To add test data:
# Run with: python -m nl2bash_server.add_data_from_scraper <path to ScrapedPages>
# In the directory with manage.py (top dir of project)

import sys, os, django, json

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


if len(sys.argv) < 1:
    print("Usage: " + sys.argv[0] + " <path to dir with data (.verify) files>")
    sys.exit()

# Uncommented to reset database
clean_all()

# Get path to data
file_path = sys.argv[1]

# Iterate through files in directory and parse JSON in .verify files
for filename in os.scandir(file_path):
    filename = os.fsdecode(filename)
    if filename.endswith('.verify'):
        with open(filename, 'rb') as f:
            # Read f into a string and parse its json
            obj = json.loads(f.read().decode('utf-8', 'ignore'))

            # Extract the english description
            eng_text = obj['title']
            eng_cmd = EnglishDescription(cmd=eng_text)

            if eng_text is not None:
                eng_cmd.save()

                # Commands are in a list now
                for bash_text in obj['commands']:
                    # Make a new CommandPair - this should also add the
                    # corresponding EnglishDescription and BashCommand
                    bash_cmd = BashCommand(cmd=bash_text)
                    if bash_text is not None:
                        bash_cmd.save()
                        ver = Verification(score=0)
                        ver.save()
                        cmd_pair = CommandPair(nl=eng_cmd, bash=bash_cmd,
                                               ver_status=ver)
                        cmd_pair.save()