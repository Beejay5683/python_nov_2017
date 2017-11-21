from __future__ import unicode_literals

from django.db import models
import bcrypt
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):

	def register(self, form_data):
		pw = str(form_data['password'])
		h_pw = bcrypt.hashpw(pw, bcrypt.gensalt())

		user = Users.objects.create(
			first_name = form_data['first_name'],
			last_name = form_data['last_name'],
			email = form_data['email'],
			password = h_pw,
		)
		return user


	def login(self, form_data):
		user = Users.objects.filter(email= form_data['email'])[0]
		return user

	def register_validation(self, form_data):
		errors = []

		if len(form_data['first_name']) < 2:
			errors.append('First Name Required')
		if len(form_data['last_name']) < 2:
			errors.append('Last Name Required')
		if len(form_data['email']) == 0 or not EMAIL_REGEX.match(form_data['email']):
			errors.append('Email Invalid')
		if len(form_data['password']) < 8:
			errors.append('password should be more than 8 characters')
		if form_data['confirm_password'] <8:
			errors.append('confirmed password should be more than 8 characters')
		if form_data['password'] != form_data['confirm_password']:
			errors.append('Passwords do not match')
		duplicate = Users.objects.filter(email = form_data['email'])
		if len(duplicate) == 1:
			errors.append('Email already exisits')

		return errors

	def login_validation(self, form_data):
		errors = []
		user = Users.objects.filter(email = form_data['email']).first()
		if user:
			pw = str(form_data['password'])
			user_password = str(user.password)
			pw_check = bcrypt.hashpw(pw.encode(), user_password.encode())
			if not user_password == pw_check:
				errors.append('Ivalid Password')
		else: 
			errors.append('Invalid Email')

		return errors


class Users(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	password = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
  	updated_at = models.DateTimeField(auto_now=True)
  	objects = UserManager()

	def __unicode__(self):
		return "id: " + str(self.id)+", First Name: "+self.first_name+", Last Name: "+ self.last_name+", email: "+ self.email+", password: " + self.password



