from django.contrib import admin
from .models import Course
# Register your models here.
@admin.register(Course)
class courseAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available',)
    search_fields = ('name','description')

