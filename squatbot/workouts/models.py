from django.db import models
from squatbot.users.models import User

# Create your models here.
class Workout(models.Model):
	name = models.CharField(max_length=50)
	date = models.DateField()
	user = models.ForeignKey(User)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Activity(models.Model):
	name = models.CharField(max_length=50)
	workout = models.ForeignKey(Workout,related_name='activities')
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Set(models.Model):
	weight = models.IntegerField()
	reps = models.IntegerField()
	activity = models.ForeignKey(Activity, related_name='sets')



