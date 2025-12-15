from django.contrib import admin
from .models import Post, Comment, Vote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updated')
    list_filter = ('created',)
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('user',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created')
    raw_id_fields = ('user', 'post', 'reply')


admin.site.register(Vote)