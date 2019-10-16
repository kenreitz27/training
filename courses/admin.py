from django.contrib import admin
from courses.models import Course, Hole, CourseTee 

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
  pass

class HoleAdmin(admin.ModelAdmin):
  pass

class CourseTeeAdmin(admin.ModelAdmin):
  pass

admin.site.register(Course, CourseAdmin)
admin.site.register(Hole, HoleAdmin)
admin.site.register(CourseTee, CourseTeeAdmin)