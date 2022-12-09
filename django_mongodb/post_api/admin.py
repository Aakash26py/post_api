from django.contrib import admin
from .models import Person
# Register your models here.
@admin.register(Person)
class personAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country']