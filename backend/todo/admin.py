from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):

    list_display = ("title", "description", "completed")

# We will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Todo, TodoAdmin)