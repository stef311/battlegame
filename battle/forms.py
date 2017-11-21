from django import forms
from .models import  Item, Message

class BuyForm(forms.Form):
    flag = forms.IntegerField(label="flags", widget = forms.TextInput(attrs={'class': 'small_input'}))

class TrainForm(forms.Form):
    warrior1 = forms.IntegerField(label="warrior1", widget = forms.TextInput(attrs={'class': 'small_input'}))
    warrior2 = forms.IntegerField(label="warrior2", widget = forms.TextInput(attrs={'class': 'small_input'}))
    warrior3 = forms.IntegerField(label="warrior3", widget = forms.TextInput(attrs={'class': 'small_input'}))


class MessageForm(forms.ModelForm):
    class Meta:
	model = Message
	fields = ["recipient", "subject", "body"]
