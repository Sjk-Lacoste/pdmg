from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Post,
    Category,
    Comment
)


class PostAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'slug',
        'status',
        'created_on'
    )
    list_filter = ("status",)
    search_fields = ['title', 'content']
    summernote_fields = '__all__'
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = '__all__'


class CommentAdmin(SummernoteModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    summernote_fields = '__all__'
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

    def __str__(self):
        return self.name


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
