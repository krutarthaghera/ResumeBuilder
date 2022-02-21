from django import forms
from django.forms.models import inlineformset_factory

from resumes.models import User, UserProjects


class UserProjectsForm(forms.ModelForm):
    class Meta:
        model = UserProjects
        fields = ['project', 'start_date', 'end_date', 'is_currently_working', 'description']


ProjectsFormSet = inlineformset_factory(
    User,
    UserProjects,
    form=UserProjectsForm,
    extra=1,
    can_delete=True
)

