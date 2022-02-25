from django.urls import path

from resumes import views
from resumes.views import *


urlpatterns = [
    # Add/Edit
    path('profiles/add/', CreateProfileView.as_view(), name='add_profile'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('templates', Template1View.as_view(), name='templates'),
#     path('profiles/add_skill', CreateSkillView.as_view(), name='add_skill'),
#     path('profiles/add_professionalexpr', CreateProfessionalExprView.as_view(), name='add_professionalexpr'),
#     path('profiles/add_educationalexpr', CreateEducationExprView.as_view(), name='add_educationexpr'),
#     path('profiles/add_projects', CreateProjectsView.as_view(), name='add_projects'),
#     path('profiles/add_language', CreateLanguageView.as_view(), name='add_language'),
#     path('profiles/add_link', CreateLinkView.as_view(), name='add_link')
#     # path('ajax/load-states/', views.load_states, name='ajax_load_states')
#     # path('profiles/edit/<uuid:uid>/', manage_profile, name='edit_profile'),
 ]
