from django import forms
from django.forms import inlineformset_factory

from core.models import User
from resumes.models import UserLink


class UserLinkForm(forms.ModelForm):

    class Meta:
        model = UserLink
        fields = ['link', 'label']

    # widgets = {
    #     'UserLink': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Link'}),
    # }

LinkFormSet = inlineformset_factory(
    User,
    UserLink,
    form=UserLinkForm,
    extra=1,
    can_delete=True
)
