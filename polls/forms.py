from django import forms
from .models import Poll

class PollForm(forms.ModelForm):
    class Meta:
        fields = ('question', 'option_one', 'option_two', 'option_three')
        model = Poll

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["question"].widget.attrs.update({'class': 'form-control'})
        self.fields["option_one"].widget.attrs.update({'class': 'form-control'})
        self.fields["option_two"].widget.attrs.update({'class': 'form-control'})
        self.fields["option_three"].widget.attrs.update({'class': 'form-control'})
