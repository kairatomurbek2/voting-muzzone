from django import forms

from web.models import PollChoice


class PollAnswerCheatForm(forms.Form):
    poll_choice = forms.ModelChoiceField(queryset=PollChoice.objects.all(), required=True)
    count = forms.IntegerField(required=True)
