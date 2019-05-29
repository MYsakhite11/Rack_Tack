from django.contrib import admin
from reversion.admin import VersionAdmin
# Register your models here.

from .models import *


# @admin.register(UserInfo)
# class UserInfoAdmin(VersionAdmin):
# 	pass


class TaskModelAdmin(admin.ModelAdmin):
	"""docstring for TaskModelAdmin"""
	list_display = ['id' ,'name_task', 'description', 'updated', 'timestamp']
	list_display_links = ['id']

	class Meta:
		model = Task


admin.site.register(Task, TaskModelAdmin)