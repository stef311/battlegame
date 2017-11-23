from django import forms
from .models import  Item, Message, Attack

class BuyForm(forms.Form):
    flag = forms.IntegerField(label="flags", widget = forms.TextInput(attrs={'class': 'small_input'}))

class TrainForm(forms.Form):
    warrior1 = forms.IntegerField(initial=0,required = False, label="warrior1", widget = forms.TextInput(attrs={'class': 'small_input'}))
    warrior2 = forms.IntegerField(initial=0,required = False, label="warrior2", widget = forms.TextInput(attrs={'class': 'small_input'}))
    warrior3 = forms.IntegerField(initial=0,required = False, label="warrior3", widget = forms.TextInput(attrs={'class': 'small_input'}))


class MessageForm(forms.ModelForm):
    class Meta:
	model = Message
	fields = ["recipient", "subject", "body"]

class AttackForm(forms.Form):
    warrior1 = forms.IntegerField(initial=0,required = False, label="warrior1", widget = forms.TextInput(attrs={'class': 'small_input'}))
    warrior2 = forms.IntegerField(initial=0,required = False, label="warrior2", widget = forms.TextInput(attrs={'class': 'small_input'}))
    warrior3 = forms.IntegerField(initial=0,required = False, label="warrior3", widget = forms.TextInput(attrs={'class': 'small_input'}))
    flag = forms.IntegerField(initial=0,required = False, label="flag", widget = forms.TextInput(attrs={'class': 'small_input'}))

