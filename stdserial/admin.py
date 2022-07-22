from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class Customer(admin.ModelAdmin):
    list_display = ("name","roll_no","country")