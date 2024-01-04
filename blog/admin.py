from django.contrib import admin
from blog.models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'author', 'published_date', 'created_date', 'status')
    empty_value_display = '-empty-'
    date_hierarchy = 'published_date'
    list_filter = ('status', 'author')
    ordering = ('-created_date',)
    search_fields = ('title', 'content')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)