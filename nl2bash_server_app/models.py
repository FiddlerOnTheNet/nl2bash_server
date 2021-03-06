from django.db import models
from django.urls import reverse
import uuid


# Create your models here.

class EnglishDescription(models.Model):
    """ Model representing an English command description. """
    cmd = models.TextField('Natural Language Command', max_length=300, null=True,
                           help_text="A natural language description of a bash command.")
    # Number of command pairs with this English description with a verification
    # score above 0
    num_verified = models.IntegerField('Number of verified command pairs', null=False,
                                       default=0)
    seen = models.BooleanField('Seen', default=False)

    def mark_as_seen(self):
        """ Mark that someone has seen this English description. """
        self.seen = True

    def inc_num_verified(self):
        """ Add 1 to the number of verified commands with this English description. """
        self.num_verified += 1

    def __str__(self):
        """ String representation of an EnglishDescription """
        return str(self.cmd)


class BashCommand(models.Model):
    """ Model representing an Bash command. """
    cmd = models.TextField('Bash Command', max_length=300,
                           help_text="A bash command.", null=True)

    def __str__(self):
        """ String representation of an BashCommand """
        return str(self.cmd)


class CommandPair(models.Model):
    """ Model representing an English/Bash command pair. """
    nl = models.ForeignKey(EnglishDescription, on_delete=models.SET_NULL, null=True)
    bash = models.ForeignKey(BashCommand, on_delete=models.SET_NULL, null=True)
    ver_status = models.ForeignKey('Verification', on_delete=models.SET_NULL, null=True)
    saved_status = models.BooleanField('Saved', default=0)

    def __str__(self):
        """ String representation of a CommandPair """
        return str(self.nl) + "\\" + str(self.bash)

    def set_saved(self):
        """ Mark this command pair as having been saved in all.nl and all.cmd. """
        self.saved_status = 1


class Verification(models.Model):
    """ Model representing the verification score for some
    English/Bash command pair. A score above zero is a positive
    verification, below zero is negative. Default value is 0. """

    score = models.IntegerField('Verification Score', default=0, null=True)

    def inc_ver_score(self):
        """ Add 1 to this verification score. """
        self.score += 1

    def dec_ver_score(self):
        """ Subtract 1 from this verification score. """
        self.score -= 1

    def __str__(self):
        """ String for representing a verification object. """
        return "Verification score: " + str(self.score)

