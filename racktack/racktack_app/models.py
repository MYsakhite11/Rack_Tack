from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User


app_name = 'racktack_app'





class Task(models.Model):
	user = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
	name_task = models.CharField(max_length=50)
	description = models.TextField()
	begin_time = models.DateField(blank=True)
	end_time = models.DateField(blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, null=True, auto_now_add=True)

	def __str__(self):
		return self.name_task


	def get_absolute_url(self):
		return "/racktack_app/%s/" %(self.id)
		# return reverse('racktack_app:update_task', kwargs={'id': self.id})

