from django.contrib import admin
from .models import Post, About
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'excerpt')

class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(About, AboutAdmin)
