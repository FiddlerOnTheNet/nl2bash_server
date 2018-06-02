# Python script that saves verified command pairs in the format used
# by Tellina:
# The data is stored in two files: all.nl and all.cm
# all.nl contains the natural language descriptions
# all.cm contains corresponding bash commands
# English descriptions and bash commands on the same lines
# form command pairs.

# Run from top project dir with: python -m nl2bash_server.save_data

import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nl2bash_server.settings")
django.setup()

from nl2bash_server_app.models import CommandPair

path_to_nl = 'all.nl'
path_to_bash = 'all.cm'

# For each command pair that has not been saved yet, add them to their
# corresponding files.

to_save = CommandPair.objects.filter(ver_status__score__gt=0).filter(saved_status=0)

# For each pair, saves it to output if needed and outputs which one it does.
for cmd_pair in to_save:
    print("Saved before?: " + str(cmd_pair.saved_status))
    with open(path_to_nl, 'a') as nl_file:
        nl_file.write(cmd_pair.nl.cmd + "\n")

    with open(path_to_bash, 'a') as bash_file:
        bash_file.write(cmd_pair.bash.cmd + "\n")

    cmd_pair.set_saved()  # Set saved to true
    cmd_pair.save()
    print("Saved after?: " + str(cmd_pair.saved_status))
