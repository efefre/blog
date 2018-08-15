from django.contrib import admin
from . import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','created','publish','author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    # raw_id_fields = ('author',) #search widget for author
    date_hierarchy = 'publish'
    ordering = ['status','publish']
admin.site.register(models.Post, PostAdmin)