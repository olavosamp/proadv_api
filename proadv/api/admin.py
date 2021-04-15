from api.models import SearchTerm, Publication

from django.contrib import admin

# Register your models here.
class SearchTermAdmin(admin.ModelAdmin):
    list_display = ('classification', 'term')
    list_filter = ['classification']

admin.site.register(Publication)
admin.site.register(SearchTerm, SearchTermAdmin)
