from django import forms
from django.forms.models import inlineformset_factory

from resumes.models import User, UserProfessionalExpr


class UserProfessionalExprForm(forms.ModelForm):

    class Meta:
        model = UserProfessionalExpr
        fields = ['job_title', 'company', 'city', 'start_date', 'end_date', 'is_currently_working', 'description']

    # widgets = {
    #     'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Job Title'}),
    #     'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Company Name'}),
    #     'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
    # }


ProfessionalExpFormSet = inlineformset_factory(
    User,
    UserProfessionalExpr,
    form=UserProfessionalExprForm,
    extra=1,
    can_delete=True
)


