from django.contrib import admin
from core.models import User
from resumes.models import UserEducation, UserProfessionalExpr, UserProjects, UserLink, Language, Skills, Level, Label, SkillLevel


admin.site.register(Level)
admin.site.register(Label)
admin.site.register(SkillLevel)
admin.site.register(Skills)


class ItemAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)


admin.site.register(User, ItemAdmin)


class SkillInline(admin.TabularInline):
    model = Skills
    fk_name = "profile"
    extra = 1


class UserEducationInline(admin.TabularInline):
    model = UserEducation
    fk_name = "user"
    extra = 1


class UserProfessionalExprInline(admin.TabularInline):
    model = UserProfessionalExpr
    fk_name = "user"
    extra = 1


class UserProjectsInline(admin.TabularInline):
    model = UserProjects
    fk_name = "user"
    extra = 1


class UserLinkInline(admin.TabularInline):
    model = UserLink
    fk_name = "user"
    extra = 1


class LanguageInline(admin.TabularInline):
    model = Language
    fk_name = "user"
    extra = 1


# @admin.register(User)
# class ProfileAdmin(admin.ModelAdmin):
#     inlines = [SkillInline, UserEducationInline, UserProfessionalExprInline, UserLinkInline, UserProjectsInline, LanguageInline]
#     model = User
#
#
#
