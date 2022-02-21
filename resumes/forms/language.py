from django import forms
from django.forms import inlineformset_factory

from resumes.models import User, Language


class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ('language', 'level')

    # widgets = {
    #     'language': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Language'}),
    #     'level': forms.Select(attrs={'class': 'form-control select2'}),
    #
    # }


LanguageFormSet = inlineformset_factory(
    User,
    Language,
    form=LanguageForm,
    extra=1,
    can_delete=True
)
