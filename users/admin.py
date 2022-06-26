from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__email', 'user__username')
    list_display = ('user',)
    list_filter = ('user__is_staff', 'user__is_superuser')


admin.site.register(Profile, ProfileAdmin)

