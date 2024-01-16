from django.contrib import admin
from mysite.models import Contact, Subscribe


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'phone_number','created_date')
    empty_value_display = '-empty-'
    date_hierarchy = 'created_date'
    list_filter = ('email',)
    ordering = ('-created_date',)
    search_fields = ('subject', 'message')

admin.site.register(Subscribe)