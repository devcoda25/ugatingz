from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')


admin.site.register(Category, CategoryAdmin)

admin.site.register(Topic,TopicAdmin)
admin.site.register(Section)
admin.site.register(Comment)
admin.site.register(Views)
