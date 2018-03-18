from django.db import models
from django import forms

class EmailForm(forms.Form):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    telefon = forms.CharField(max_length=255)
    streetname = forms.CharField(max_length=255)
    plz = forms.CharField(max_length=255)
    ort = forms.CharField(max_length=255)
    telefon = forms.CharField(max_length=255)
    #auswahl = forms.CharField(max_length=255)
    #emailadresse = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    botcheck = forms.CharField(max_length=5)
    message = forms.CharField()
    messageHidden = forms.CharField()

class BewerbungForm(forms.Form):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    telefon = forms.CharField(max_length=255)
    streetname = forms.CharField(max_length=255)
    plz = forms.CharField(max_length=255)
    ort = forms.CharField(max_length=255)
    telefon = forms.CharField(max_length=255)
    #auswahl = forms.CharField(max_length=255)
    #emailadresse = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    botcheck = forms.CharField(max_length=5)
    message = forms.CharField()
    #messageHidden = forms.CharField()
