from django.db import models
from django.utils import timezone


# this line defines our model, it is an object
# class is a keyword that indicates we are defining an object
# post is the name of our model (always starts with uppercase letter)
# models.Model means the Post is a Django Model,
# so to save it in the database

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published.date = timezone.now()
		self.save()

	def __str__(self):
		return self.title