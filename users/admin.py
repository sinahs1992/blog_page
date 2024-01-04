from django.contrib import admin
from users.models import SiteAdmin, Customer, User

@admin.register(SiteAdmin)
class SiteAdminAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'id')
    empty_value_display = "-empty-"
    search_fields = ["username", "first_name", "last_name"]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'id','is_vip')
    empty_value_display = "-empty-"
    search_fields = ["username", "first_name", "last_name"]


admin.site.register(User)

