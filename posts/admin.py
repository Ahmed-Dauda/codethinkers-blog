from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'author')
    list_filter = ('date_post',)

admin.site.register(Post, PostAdmin)

