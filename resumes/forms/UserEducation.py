from django import forms
from django.forms.models import inlineformset_factory

from resumes.models import User, UserEducation


class UserEducationForm(forms.ModelForm):

    class Meta:
        model = UserEducation
        fields = ['institute_name', 'institute_city', 'degree', 'graduation_date', 'education_description']


EducationFormSet = inlineformset_factory(
    User,
    UserEducation,
    form=UserEducationForm,
    extra=1,
    can_delete=True
)
