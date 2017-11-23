from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.central, name = "central"),
    url(r"^info/$", views.info, name = "info"),
    url(r"^buildings/$", views.buildings, name = "buildings"),
    url(r"^units/$", views.units, name = "units"),
    url(r"^items/$", views.items, name = "items"),
    url(r"^players/$", views.players, name = "players"),
    url(r"^players/(?P<username>[-\w]+)/$", views.player, name = "player"),
    url(r"^attack/(?P<username>[-\w]+)/$", views.attack, name = "attack"),
    url(r"^send_message/(?P<username>[-\w]+)/$", views.send_message, name = "send_message"),
    url(r"^all_messages/$", views.all_messages, name = "all_messages"),
    url(r"^message/(?P<msg_id>[0-9]+)/$", views.message, name = "message"),
    url(r"^send_message/$", views.send_message, name = "send_message"),
    url(r"^sent_messages/$", views.sent_messages, name = "sent_messages"),
    url(r"^received_messages/$", views.received_messages, name = "received_messages"),
    url(r"^buildings/army/$", views.army, name = "army"),
    url(r"^buildings/market/$", views.market, name = "market"),
    url(r"^buildings/central/$", views.central, name = "central"),
    url(r"^buildings/market/buy/$", views.buy_items, name = "buy_items"),
    url(r"^buildings/army/train/$", views.train_units, name = "train_units"),
    url(r"^buildings/(?P<building_name>[-\w]+)/build/$", views.upgrade_building, name = "upgrade_building"),
    url(r"^buildings/(?P<building_name>[-\w]+)/build/done/$", views.upgrade_building_done, name = "upgrade_building_done"),
]

