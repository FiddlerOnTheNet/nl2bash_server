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

    def __str__(self):
        """ String representation of a CommandPair """
        return str(self.nl) + "\\" + str(self.bash)

    # def get_absolute_url(self):
    #     """ Returns the url to access a detailed record for this CommandPair. """
    #     return reverse("command_pair_detail", args=[str(self.id)])


class Verification(models.Model):
    """ Model representing the verification score for some
    English/Bash command pair. A score above zero is a positive
    verification, below zero is negative. Default value is 0. """

    score = models.IntegerField('Verification Score', default=0, null=True)

    def __str__(self):
        """ String for representing a verification object. """

        return "Verification score: " + str(self.score)


# class CommandPairInstance(models.Model):
#     """ Model representing a specific command pair. """
#
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     cmd_pair = models.ForeignKey('CommandPair', on_delete=models.SET_NULL, null=True)
#
#     class Meta:
#         ordering = ['id']
#
#     def __str__(self):
#         """ String for representing the object. """
#
#         return self.cmd_pair
