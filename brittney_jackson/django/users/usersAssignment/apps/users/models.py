from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email_address = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
  	updated_at = models.DateTimeField(auto_now=True)