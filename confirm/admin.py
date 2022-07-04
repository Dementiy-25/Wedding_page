from django.contrib import admin, messages
from .models import Wedding, Country
from django.db.models import QuerySet
# Register your models here.

admin.site.register(Country)

class GenderFilter(admin.SimpleListFilter):
    title = 'Filter by gender'
    parameter_name = 'gender'
    def lookups(self, request, model_admin):
        return [
            ('male', 'Male'),
            ('female', 'Female')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == 'male':
            return queryset.filter(gender='m')
        if self.value() == 'female':
            return queryset.filter(gender='f')

@admin.register(Wedding)
class WeddingAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = ['first_name', 'last_name', 'age', 'country', 'gender']
    list_editable = ['last_name', 'age', 'country', 'gender']
    ordering = ['last_name', 'first_name']
    list_per_page = 10
    search_fields = ['first_name']
    list_filter = ['first_name', 'last_name', GenderFilter]

