# Python script that adds test data
# Format: From ScrapedPages - top line is the English command description,
# subsequent lines are bash commands suggested to match that English
# description.
# This script takes a directory of those files, then creates CommandPair
# entries in the database for them.

import sys, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nl2bash_server.settings")
django.setup()

from nl2bash_server_app.models import CommandPair, EnglishDescription, BashCommand

if len(sys.argv) < 1:
    print("Usage: " + sys.argv[0] + " <path to dir with data (.verify) files>")
    sys.exit()

# Get path to data
file_path = sys.argv[1]

# Iterate through files in directory and operate on the .verify files
for filename in os.scandir(file_path):
    filename = os.fsdecode(filename)
    if filename.endswith(".verify"):
        with open(filename) as f:
            # Extract the english description, remove trailing newline
            eng_text = cmd=f.readline().strip()
            eng_cmd = EnglishDescription(cmd=eng_text)

            # Check if this English command is already in the DB
            if not EnglishDescription.objects.filter(cmd=eng_text).exists() \
                    and eng_text is not None:
                eng_cmd.save()
                for line in f:
                    # Make a new CommandPair - this should also add the
                    # corresponding EnglishDescription and BashCommand
                    bash_text = line.strip()
                    bash_cmd = BashCommand(cmd=bash_text)
                    if bash_text is not None:
                        bash_cmd.save()
                        cmd_pair = CommandPair(nl=eng_cmd, bash=bash_cmd)
                        cmd_pair.save()
