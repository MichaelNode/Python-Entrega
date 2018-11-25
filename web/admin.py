from django.contrib import admin
from web.models import *


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'description',
        'blog_date',
        'last_modification'
    )
    list_filter = [
        'blog_date'
    ]
    search_fields = [
        'author__username'
    ]
    fieldsets = [
        ['Create Blog', {
            'fields': ['author']
        }],
        ['Blog info', {
            'fields': ['title', 'description'],
            'description': 'Info related with owner and more...',
        }]
    ]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'blog_id',
        'author',
        'cat_id',
        'title',
        'content',
        'image',
        'status',
        'pos_date',
        'last_modification'
    )
    list_filter = [
        'pos_date'
    ]
    search_fields = [
        'author__username'
    ]
    fieldsets = [
        ['Create Post', {
            'fields': ['author', 'blog_id','cat_id']
        }],
        ['Blog info', {
            'fields': ['title', 'status', 'content','image']
        }]
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'author',
        'com_date',
        'last_modification'
    )
    list_filter = [
        'com_date'
    ]
    search_fields = [
        'author__username'
    ]
    fieldsets = [
        ['Create Comments', {
            'fields': ['author', 'post_id']
        }],
        ['Comments info', {
            'fields': ['title', 'content']
        }]
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'cat_id',
        'name',
        'user_reg'
    )
    list_filter = [
        'date_reg'
    ]
    search_fields = [
        'name'
    ]
    fieldsets = [
        ['Create Category', {
            'fields': ['user_reg']
        }],
        ['Category info', {
            'fields': ['name']
        }]
    ]


