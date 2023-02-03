from django.db import models

# Create your models here.

class Register(models.Model):
	name = models.CharField(max_length = 20)
	lastname = models.CharField(max_length = 20)
	email = models.EmailField(blank = True)
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 16)
	updated = models.DateTimeField(auto_now_add = True)
	created = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.username