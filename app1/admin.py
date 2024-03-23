from django.contrib import admin
from app1.models import Profile
from app1.models import Task
from django.contrib.auth.models import User


class ProfileAdmin(admin.ModelAdmin):
    pass

class TaskAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    list_filter = ["username"]
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Task, TaskAdmin)
# admin.site.register(User, UserAdmin)