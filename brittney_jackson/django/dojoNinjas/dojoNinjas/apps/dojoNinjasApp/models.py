from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
	name = models.CharField(max_length=45)
	city = models.CharField(max_length=45)
	state = models.CharField(max_length=45)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True) 

	def __unicode__(self):
		return 'id: '+str(self.id)+', name: '+ self.name+', city: '+self.city+ ', state: '+self.state+ ', description: '+self.desc

class Ninja(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	dojo = models.ForeignKey(Dojo, related_name="ninjas")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True) 

	def __unicode__(self):
		return 'id: '+str(self.id)+', first name: '+ self.first_name+', last name: '+self.last_name+ ', dojo: '+str(self.dojo.id)
