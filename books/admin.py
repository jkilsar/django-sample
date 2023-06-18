from django.contrib import admin

from .models import Books

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}
