from django.contrib import admin
from .models import Role,Members,Events
# Register your models here.

admin.site.register(Role)
admin.site.register(Members)
admin.site.register(Events)