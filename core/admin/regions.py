from django.contrib import admin
from core.models import Country, State, City
from core.admin.resources import CountryAdmin, StateAdmin, CityAdmin


admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
