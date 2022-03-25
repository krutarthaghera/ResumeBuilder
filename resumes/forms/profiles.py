from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from core.models import User, State
from resumes.custom_formset_layout_object import Formset


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'profile_image', 'date_of_birth', 'phone_number', 'country',
                  'state', 'about')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # self.fields['state'].queryset = State.objects.none()
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('first_name'),
                Field('last_name'),
                Field('email'),
                Field('profile_image'),
                Field('date_of_birth'),
                Field('phone_number'),
                Field('country'),
                Field('about'),
                Fieldset('Skills',
                         Formset('user_skills')
                         ),
                Fieldset('Professional Experience',
                         Formset('user_professional_expr')
                         ),
                Fieldset('Education Details',
                         Formset('user_education')
                         ),
                Fieldset('Projects',
                         Formset('user_projects')
                         ),
                Fieldset('Language',
                         Formset('user_language')
                         ),
                Fieldset('Links',
                         Formset('user_link')
                         ),
                # Field('note'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
            )
        )