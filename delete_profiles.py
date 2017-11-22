import os, sys

# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "battlegame.settings")

# This is so models get loaded.

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from account.models import Profile, Belongings
from django.contrib.auth.models import User


for user in User.objects.all():
    if user.username != "admin":
	belongings = Belongings.objects.filter(user = user).delete()
	profile = Profile.objects.filter(user = user).delete()
        user.delete()
