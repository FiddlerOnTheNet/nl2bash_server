from django.shortcuts import render
from .models import CommandPair, Verification, EnglishDescription, BashCommand
from django.views import generic


# Create your views here.
def get_next_unverified():
    """ Retrieves the next English command from the database
    that has no verified bash commands associated with it. If
    no such English commands exist, it returns None for now. """
    return EnglishDescription.objects.filter(num_verified__gt=0).first()


def tester(request):
    """ View function that handles http requests from the
    Tester UI. Provides the tester UI with an English command
    and three associated bash commands to verify. """

    # Get the next English command from the database that has
    # no verified bash commands associated with it.
    eng_cmd = get_next_unverified()

    # Get the list of command pairs with this english command
    # description
    cmd_pair_list = CommandPair.objects.filter(nl__exact=eng_cmd)

    # Extract up to five possible bash commands to display

    return render(
        request,
        'tester.html',
        context={"english_command": eng_cmd, },
    )

def fetch(request):
    """ Handles fetching """

