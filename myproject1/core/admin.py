from django.contrib import admin

from models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    search_fields = ['title']

admin.site.register(Person, PersonAdmin)
admin.site.register(Book, BookAdmin)
