from django.shortcuts import render
from .models import CommandPair, Verification, EnglishDescription, BashCommand
from django.views import generic


# Create your views here.
def get_next_unverified():
    """ Retrieves the next English command from the database
    that has no verified bash commands associated with it. If
    no such English commands exist, it returns None for now. """
    return EnglishDescription.objects.filter(num_verified=0).first()


def tester(request):
    """ View function that handles http requests from the
    Tester UI. Provides the tester UI with an English command
    and three associated bash commands to verify. """

    # Get the next English command from the database that has
    # no verified bash commands associated with it.
    eng_cmd = str(get_next_unverified())

    # Get the list of command pairs with this english command
    # description
    cmd_pair_list = CommandPair.objects.filter(nl__cmd__exact=eng_cmd)[:5]

    # Extract up to five possible bash commands to display
    bash_cmd_list = []
    for cmd_pair in cmd_pair_list:
        bash_cmd_list.append(str(cmd_pair.bash))

    return render(
        request,
        'tester.html',
        context={"english_command": eng_cmd,
                 "bash_cmd_list": bash_cmd_list},
    )

def submit(request):
    """ Handle the event when the user presses the submit button."""

