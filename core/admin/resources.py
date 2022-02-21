from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin


from core.models import Country, State, City


class CountryResource(resources.ModelResource):
    code = Field(attribute='code', column_name='iso3')

    class Meta:
        model = Country
        fields = ('id', 'name', 'code')
        exclude = ('status', 'created_by', 'updated_by', 'created_at', 'updated_at', 'deleted_by',
                   'deleted_at')


class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource


class StateResource(resources.ModelResource):
    country = Field(attribute='country', column_name='country_id', widget=ForeignKeyWidget(Country, 'id'))
    code = Field(attribute='code', column_name='state_code')

    class Meta:
        model = State
        fields = ('id', 'country', 'name', 'code')
        exclude = ('status', 'created_by', 'updated_by', 'created_at', 'updated_at', 'deleted_by',
                   'deleted_at')


class StateAdmin(ImportExportModelAdmin):
    resource_class = StateResource


class CityResource(resources.ModelResource):
    state = Field(attribute='state', column_name='state_id', widget=ForeignKeyWidget(State, 'id'))

    class Meta:
        model = City
        fields = ('id', 'state', 'name')
        exclude = ('status', 'created_by', 'updated_by', 'created_at', 'updated_at', 'deleted_by',
                   'deleted_at')


class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource
