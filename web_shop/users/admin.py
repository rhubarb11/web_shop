from django.contrib import admin
from .models import UserDetails


class UserDetailsAdmin(admin.ModelAdmin):
        search_fields = ['user__username', 'user__email']

admin.site.register(UserDetails, UserDetailsAdmin)
