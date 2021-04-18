from api.models import SearchTerm, Publication

from django.contrib import admin

# Register your models here.
class SearchTermAdmin(admin.ModelAdmin):
    list_display = ('id', 'classification', 'term')
    list_filter = ['classification']
    ordering =  ['id']

class PublicationAdmin(admin.ModelAdmin):
    list_display = ['id']
    ordering =  ['id']


admin.site.register(Publication, PublicationAdmin)
admin.site.register(SearchTerm, SearchTermAdmin)
