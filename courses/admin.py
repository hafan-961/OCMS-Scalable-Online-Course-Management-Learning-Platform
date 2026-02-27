from django.contrib import admin

# Register your models here.
from .models import Category, Course, Module, Lecture

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # This uses 'name' because that is what we set in your models.py earlier
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)} 

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor_id', 'category_id', 'price', 'level', 'is_published')

admin.site.register(Module)
admin.site.register(Lecture)