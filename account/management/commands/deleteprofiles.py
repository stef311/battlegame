from django.core.management.base import BaseCommand, CommandError
from account.models import Profile, Belongings

class Command(BaseCommand):
    help = "Deletes all profiles and belongings"

    def add_argument(self,parser):
	pass

    def handle(self, *args, **kwargs):
	try:
	    print("I am here")
	except Exception as e:
	    raise CommandError(repr(e))
