from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'category', 'status', 'promote', 'created_time')
    search_fields = ('author', 'title', 'body', 'category')
    list_filter = ('category', 'status', 'promote', 'created_time')


admin.site.register(Post, PostAdmin)
