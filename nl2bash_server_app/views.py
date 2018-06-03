from django.shortcuts import render, redirect
from .models import CommandPair, Verification, EnglishDescription, BashCommand
from django.views import generic
from django.http import HttpResponseRedirect

# Note: print statements aren't for debugging; they allow the owner of the
# server to understand what the testers are doing on the site.

# Create your views here.
def tester_init(request):
    """ Sets up the session and redirects to the tester. """
    #if "seen" not in request.session:
    #    request.session["seen"] = []

    return redirect(tester)


def get_next_unverified():
    """ Retrieves the next English command from the database
    that has no verified bash commands associated with it. If
    no such English commands exist, it returns None for now. """
    unverified = EnglishDescription.objects.filter(seen=False)

    return unverified[0]


def tester(request):
    """ View function that handles http requests from the
    Tester UI. Provides the tester UI with an English command
    and three associated bash commands to verify. """
    print("Entering tester view.")

    # Get the next English command from the database that has
    # no verified bash commands associated with it, and has
    # not yet been seen by the user.
    eng_cmd = str(get_next_unverified())

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
        # Checked boxes should only have elements if things were checked.
        checked_boxes = []
        postDict = dict(request.POST)
        if 'cBox' in postDict.keys():
            checked_boxes = postDict['cBox']
        eng_text = request.session['current_eng_text']
        current_nl = EnglishDescription.objects.get(cmd__exact=eng_text)

        current_nl.mark_as_seen()
        current_nl.save()

        # Update the verification score for each of the checked
        # command pairs.
        for bash_text in checked_boxes:
            print("Checked: " + str(bash_text))
            # Get the CommandPair this bash_text is from
            cmd_pair = CommandPair.objects.filter(nl__cmd__exact=eng_text)\
                .get(bash__cmd__exact=bash_text)

            cmd_pair.ver_status.inc_ver_score()  # Add 1 to verification score

            #cmd_pair.nl.inc_num_verified()  # Mark that someone has looked at this cmdpair
            cmd_pair.ver_status.save()
            cmd_pair.nl.save()
            cmd_pair.save()

        # Unchecked pairs can be inferred using
        # values stored in session.
        bash_cmd_list = request.session['current_bash_list']
        #print("Current bash_cmd_list: " + str(bash_cmd_list))
        for bash_text in bash_cmd_list:
            cmd_pair = CommandPair.objects.filter(nl__cmd__exact=eng_text) \
                .get(bash__cmd__exact=bash_text)
            cmd_pair.nl.inc_num_verified()
            #cmd_pair.nl.mark_as_seen() # Mark that someone has looked at this cmdpair

            if bash_text not in checked_boxes:
                #print("Not checked: " + str(bash_text))
                #cmd_pair.ver_status.dec_ver_score()
                #print("Ver score after decrement: " + str(cmd_pair.ver_status.score))
                cmd_pair.ver_status.save()
                cmd_pair.save()

        # Update the "seen" session value so that the user does not see the same
        # question twice.
        #print("Current command seen? (should be true): " + str(current_nl.seen))
        #request.session["seen"].append(eng_text)
        #print("submit seen: " + str(request.session["seen"]))

    return redirect(tester)


def skip(request):
    """ Handle the event when the user presses the skip button.
    This loads new commands without updating any verification
    scores. """

    # Update the "seen" session value so that the user does not see the same
    # question twice.
    #print("current Eng: " + str(request.session['current_eng_text']))
    #request.session["seen"].append(request.session['current_eng_text'])
    #print("skip seen: " + str(request.session["seen"]))

    return redirect(tester)
