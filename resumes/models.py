import uuid
from django.db import models
from core.models import Base, User


class Skills(models.Model):
    SKILL_LEVEL=(
        ('novice', 'NOVICE'),
        ('beginner', 'BEGINNER'),
        ('skillful', 'SKILLFUL'),
        ('experienced', 'EXPERIENCED'),
        ('expert', 'EXPERT')
    )
    skill_id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_skills', db_column='profile_id',
                                null=True, blank=True)
    skill_name = models.CharField(max_length=100, null=True, blank=True)
    skill_level = models.CharField(max_length=50, choices=SKILL_LEVEL)

    class Meta:
        # managed = False
        db_table = 'skills'
        verbose_name_plural = "Skills"

    # def __str__(self):
    #     return self.skill_name


class UserProfessionalExpr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_currently_working = models.BooleanField()
    description = models.CharField(max_length=2000, blank=True)

    # def __str__(self):
    #     return self.job_title


class UserEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=50)
    institute_city = models.CharField(max_length=50, blank=True)
    degree = models.CharField(max_length=50)
    graduation_date = models.DateField(blank=True, null=True)
    education_description = models.CharField(max_length=2000, blank=True)

    # def __str__(self):
    #     return self.institute_name


class UserProjects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.CharField(max_length=256)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_currently_working = models.BooleanField()
    description = models.CharField(max_length=5000)


class UserLink(models.Model):
    LINK_LABELS = (
        ('github', 'GITHUB'),
        ('linkedin', 'LINKEDIN'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(blank=True, null=True, max_length=500)
    label = models.CharField(max_length=50, choices=LINK_LABELS)

    # def __str__(self):
    #     return self.link


class Language(models.Model):
    LANGUAGE_LEVEL = (
        ('native speaker', 'NATIVE SPEAKER'),
        ('highly proficient', 'HIGHLY PROFICIENT'),
        ('very good command', 'VERY GOOD COMMAND'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    level = models.CharField(max_length=50, choices=LANGUAGE_LEVEL)

    # def __str__(self):
    #     return self.language


class Templates(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)