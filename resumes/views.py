from datetime import datetime
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from core.models import User, State
from resumes.forms.userLink import LinkFormSet
from resumes.models import Skills, UserProfessionalExpr, UserEducation, Language, UserLink, UserProjects
from resumes.forms import *

from django.views.generic.edit import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from django.db import transaction


# def load_states(request):
#     country_id = request.GET.get('country')
#     states = State.objects.filter(country_id=country_id).order_by('name')
#     return render(request, 'hr/state_dropdown_list_options.html', {'states': states})


class CreateProfileView(FormView):
    template_name = 'Profiles/profile_management.html'
    form_class = ProfileForm
    success_url = reverse_lazy('add_skill')

    def form_valid(self, form):
        return super(CreateProfileView, self).form_valid(form)


class CreateSkillView(FormView):
    template_name = 'Profiles/profile_management.html'
    form_class = SkillForm
    success_url = reverse_lazy('add_professionalexpr')

    def form_valid(self, form):
        form.save()
        return super(CreateSkillView, self).form_valid(form)


class CreateProfessionalExprView(FormView):
    template_name = 'Profiles/profile_management.html'
    form_class = UserProfessionalExprForm
    success_url = reverse_lazy('add_educationexpr')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user = self.request.user
        user.save()
        return super(CreateProfessionalExprView, self).form_valid(form)


class CreateEducationExprView(FormView):
    template_name = 'Profiles/profile_management.html'
    form_class = UserEducationForm
    success_url = reverse_lazy('add_projects')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user = self.request.user
        user.save()
        return super(CreateEducationExprView, self).form_valid(form)


class CreateProjectsView(FormView):
    template_name = 'Profiles/profile_management.html'
    form_class = UserProjectsForm
    success_url = reverse_lazy('add_language')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user = self.request.user
        user.save()
        return super(CreateProjectsView, self).form_valid(form)


class CreateLanguageView(FormView):
    template_name = 'Profiles/profile_management.html'
    form_class = LanguageForm
    success_url = reverse_lazy('add_link')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user = self.request.user
        user.save()
        return super(CreateLanguageView, self).form_valid(form)


class CreateLinkView(FormView):
    template_name = 'Profiles/profile_management.html'
    form_class = UserLinkForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user = self.request.user
        user.save()
        return super(CreateLinkView, self).form_valid(form)


# class CreateProfileView(CreateView):
#     model = User
#     template_name = 'Profiles/profile_management.html'
#     form_class = ProfileForm
#     success_url = None
#
#     def get_context_data(self, **kwargs):
#         data = super(CreateProfileView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['user_skills'] = SkillFormSet(self.request.POST)
#             data['user_professional_expr'] = ProfessionalExpFormSet(self.request.POST)
#             data['user_education'] = EducationFormSet(self.request.POST)
#             data['user_projects'] = ProjectsFormSet(self.request.POST)
#             data['user_language'] = LanguageFormSet(self.request.POST)
#             data['user_link'] = LinkFormSet(self.request.POST)
#         else:
#             data['user_skills'] = SkillFormSet()
#             data['user_professional_expr'] = ProfessionalExpFormSet()
#             data['user_education'] = EducationFormSet()
#             data['user_projects'] = ProjectsFormSet()
#             data['user_language'] = LanguageFormSet()
#             data['user_link'] = LinkFormSet()
#         return data
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         user_skills = context['user_skills']
#         user_professional_expr = context['user_professional_expr']
#         user_education = context['user_education']
#         user_projects = context['user_projects']
#         user_language = context['user_language']
#         user_link = context['user_link']
#         with transaction.atomic():
#             form.instance.created_by = self.request.user
#             self.object = form.save()
#
#             if user_skills.is_valid():
#                 user_skills.instance = self.object
#                 user_skills.save()
#
#             if user_professional_expr.is_valid():
#                 user_professional_expr.instance = self.object
#                 user_professional_expr.save()
#
#             if user_education.is_valid():
#                 user_education.instance = self.object
#                 user_education.save()
#
#             if user_projects.is_valid():
#                 user_projects.instance = self.object
#                 user_projects.save()
#
#             if user_language.is_valid():
#                 user_language.instance = self.object
#                 user_language.save()
#
#             if user_link.is_valid():
#                 user_link.instance = self.object
#                 user_link.save()
#
#         return super(CreateProfileView, self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('dashboard')