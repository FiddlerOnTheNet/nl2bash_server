from django.db import models
from django.urls import reverse
import uuid
import django.utils.timezone as timezone
from datetime import timedelta

# Create your models here.

class EnglishDescription(models.Model):
    """ Model representing an English command description. """
    cmd = models.TextField('Natural Language Command', max_length=300, null=True,
                           help_text="A natural language description of a bash command.")
    # Number of command pairs with this English description with a verification
    # score above 0
    num_verified = models.IntegerField('Number of verified command pairs', null=False,
                                       default=0)
    time_accessed = models.DateTimeField(default=timezone.now())

    def inc_num_verified(self):
        """ Add 1 to the number of verified commands with this English description. """
        self.num_verified += 1

    def check_time_threshold(self, thresh):
        """ Checks if at least thresh minutes have passed since last updating the
        time accessed. """
        start_time = self.time_accessed
        end_time = timezone.now()
        return (end_time - start_time) > timedelta(minutes=thresh)

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

    #def set_time_accessed(self):
    #    """ Sets the timefield to when this method is called. """
    #    self.time_accessed = timezone.now()

        # def get_absolute_url(self):
    #     """ Returns the url to access a detailed record for this CommandPair. """
    #     return reverse("command_pair_detail", args=[str(self.id)])


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

