from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Task)
admin.site.register(Team)
admin.site.register(Worker)
admin.site.register(AdminUser)
admin.site.register(AskToBeAdmin)
