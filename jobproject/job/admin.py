from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Certification)
admin.site.register(HardSkill)
admin.site.register(SoftSkill)
admin.site.register(ToolAndTechnology)
admin.site.register(Education)

# Register your models here.
