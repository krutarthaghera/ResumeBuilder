import uuid
from django.db import models
from core.models.base import Base


class Country(Base):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    code = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'countries'
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class State(Base):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='countries',
        db_column='country_id',
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    code = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'states'
        verbose_name_plural = "States"

    def __str__(self):
        return self.name


class City(Base):
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='states',
        db_column='state_id',
    )
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'cities'
        verbose_name_plural = "Cities"

    # def __str__(self):
    #     return self.name

