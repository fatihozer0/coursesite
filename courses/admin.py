from django.contrib import admin
from . models import Course

@admin.site.register(Course)
class CourseAdmin(admin.ModelAdmin):
    