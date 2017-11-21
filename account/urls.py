from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^login/$", views.user_login, name = "user_login"),
    url(r"^register/$", views.register, name = "register"),
    url(r"^dashboard/$", views.dashboard, name = "dashboard"),
    url(r"^edit/$", views.edit, name = "edit"),
    url(r"^logout/$", views.user_logout, name = "user_logout"),
]
