from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
  	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "id: " + str(self.id) + ", first name: " + self.first_name+ ", last name: " + self.last_name+ ", email: " + self.email



class Book(models.Model):
	name = models.CharField(max_length=45)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	uploader = models.ForeignKey(User, related_name="uploaded_books")
	liked_users = models.ManyToManyField(User, related_name="liked_books")
	

	def __unicode__(self):
		return 'id: '+str(self.id)+ ", name: " + self.name+ ", description: " + self.desc



class Like(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)




