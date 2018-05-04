from django.contrib import admin
from .models import EnglishDescription, BashCommand, CommandPair, Verification

# Register your models here.
admin.site.register(EnglishDescription)
admin.site.register(BashCommand)
admin.site.register(CommandPair)
admin.site.register(Verification)
