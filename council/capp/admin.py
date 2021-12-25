from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(StudentProfile)
admin.site.register(Union)
admin.site.register(UnionForm)
admin.site.register(Candidate)

