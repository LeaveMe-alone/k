from django.contrib import admin

from .models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    search_fields = ['title', 'content']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)


class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']
