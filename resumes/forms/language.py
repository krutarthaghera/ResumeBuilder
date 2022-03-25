from django import forms
from django.forms import inlineformset_factory

from resumes.models import User, Language


class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ('language', 'level')


LanguageFormSet = inlineformset_factory(
    User,
    Language,
    form=LanguageForm,
    extra=1,
    can_delete=True
)
