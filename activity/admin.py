from django.contrib import admin
from .models import Comment, Relation, Vote


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'reply', 'body', 'created_time')
    search_fields = ('user', 'post', 'body')
    list_filter = ('created_time',)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Relation)
admin.site.register(Vote)

