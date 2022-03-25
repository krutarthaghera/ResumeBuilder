from django import forms
from django.forms.models import inlineformset_factory

from resumes.models import User, Skills


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skills
        fields = ('skill_name', 'skill_level')


SkillFormSet = inlineformset_factory(
    User,
    Skills,
    form=SkillForm,
    fk_name='profile',
    extra=1,
    can_delete=True
)
