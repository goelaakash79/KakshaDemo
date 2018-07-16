from django.contrib import admin

# Register your models here.
from .models import Student, MarkAttendance

admin.site.register(Student)
admin.site.register(MarkAttendance)

