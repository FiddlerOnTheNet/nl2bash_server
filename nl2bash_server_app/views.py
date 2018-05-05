from django.shortcuts import render, redirect
from .models import CommandPair, Verification, EnglishDescription, BashCommand
from django.views import generic
from django.http import HttpResponseRedirect


# Create your views here.
def tester_init(request):
    """ Sets up the session and redirects to the tester. """
    request.session["seen"] = []

    return redirect(tester)


def get_next_unverified(seen):
    """ Retrieves the next English command from the database
    that has no verified bash commands associated with it. If
    no such English commands exist, it returns None for now. """
    unverified = EnglishDescription.objects.filter(num_verified=0)
    unseen = []

    for eng_cmd in unverified:
        if eng_cmd.cmd not in seen:
            unseen.append(eng_cmd)

    if len(unseen) == 0:
        return None
    return unseen[0]


def tester(request):
    """ View function that handles http requests from the
    Tester UI. Provides the tester UI with an English command
    and three associated bash commands to verify. """

    # Get the next English command from the database that has
    # no verified bash commands associated with it, and has
    # not yet been seen by the user.
    eng_cmd = str(get_next_unverified(request.session["seen"]))

    # Get the list of command pairs with this english command
    # description
    # Extract up to five possible bash commands to display
    cmd_pair_list = CommandPair.objects.filter(nl__cmd__exact=eng_cmd)[:5]

    bash_cmd_list = []
    for cmd_pair in cmd_pair_list:
        bash_cmd_list.append(str(cmd_pair.bash))

    # Update session info, add data to be passed between views
    request.session['current_eng_text'] = eng_cmd
    request.session['current_bash_list'] = bash_cmd_list

    return render(
        request,
        'tester.html',
        context={"english_command": eng_cmd,
                 "bash_cmd_list": bash_cmd_list},
    )


def submit(request):
    """ Handle the event when the user presses the submit button.
    This updates the verification score for the displayed command
    pairs, and then loads new commands. """

    # request.POST is a Django QueryDict containing the form
    # information. This can be directly casted into a dict, then
    # the list of bash commands can be extracted.
    if request.method == "POST":
        checked_boxes = dict(request.POST)['cBox']
        eng_text = request.session['current_eng_text']

        # Update the verification score for each of the checked
        # command pairs.
        for bash_text in checked_boxes:
            # Get the CommandPair this bash_text is from
            cmd_pair = CommandPair.objects.filter(nl__cmd__exact=eng_text)\
                .get(bash__cmd__exact=bash_text)

            print(cmd_pair)
            cmd_pair.ver_status.inc_ver_score()  # Add 1 to verification score
            cmd_pair.nl.inc_num_verified()  # Inc number of verified commands for
                                            # this English description
            cmd_pair.nl.save()
            cmd_pair.save()

        # Unchecked pairs can be inferred using
        # values stored in session.
        bash_cmd_list = request.session['current_bash_list']
        for bash_text in bash_cmd_list:
            if bash_text not in checked_boxes:
                cmd_pair = CommandPair.objects.filter(nl__cmd__exact=eng_text) \
                    .get(bash__cmd__exact=bash_text)
                cmd_pair.ver_status.dec_ver_score()

                cmd_pair.ver_status.save()

        # Update the "seen" session value so that the user does not see the same
        # question twice.
        request.session["seen"].append(eng_text)

    return redirect(tester)


def skip(request):
    """ Handle the event when the user presses the skip button.
    This loads new commands without updating any verification
    scores. """

