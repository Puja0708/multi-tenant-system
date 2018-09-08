from __future__ import unicode_literals, absolute_import

from django import forms

from teams.models import Teams


class CreateTeamForm(forms.ModelForm):
    name = forms.CharField()
    max_members = forms.IntegerField()

    class Meta:
        model = Teams
        fields = '__all__'