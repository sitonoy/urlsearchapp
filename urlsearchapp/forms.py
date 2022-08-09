from django import forms
from .models import Searchlist


class InputForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = "form-control"

    class Meta:
        model = Searchlist
        exclude = ['registered_date', 'result', 'proba']
