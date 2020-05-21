from django import forms
from .models import *


class Recruit_registration(forms.Form):
    name = forms.CharField(max_length=100)
    planets = [(planet, planet.name) for planet in Planet.objects.all()]
    planet = forms.ChoiceField(choices=planets, required=True)
    age = forms.IntegerField()
    email = forms.EmailField()


class Sith_registration(forms.Form):
     siths = [(sith, sith.name) for sith in Sith.objects.all()]
     sith = forms.ChoiceField(choices=siths, required=True)
     recruits = [(recruit, recruit.name) for recruit in Recruit.objects.all()]
     recruit = forms.ChoiceField(choices=recruits, required=True)


class Test_for_recruit(forms.Form):
    answer = forms.CharField(max_length=100)
