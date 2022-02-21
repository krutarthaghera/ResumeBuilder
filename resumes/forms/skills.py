from django import forms
from django.forms.models import inlineformset_factory

from resumes.models import User, Skills


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skills
        fields = ('skill_name', 'skill_level')

        # widgets = {
        #     'skill_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Skill'}),
        #     'skill_level': forms.Select(attrs={'class': 'form-control select2'}),
        # }


SkillFormSet = inlineformset_factory(
    User,
    Skills,
    form=SkillForm,
    fk_name='profile',
    extra=1,
    can_delete=True
)
