from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
  model = Comment
  extra = 0

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'body', 'poster', 'created_at', 'updated_at')
  list_filter = ('poster', 'created_at', 'updated_at')

  inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('title', 'body', 'commenter', 'post', 'created_at', 'updated_at')
  list_filter = ('commenter', 'post', 'created_at', 'updated_at')