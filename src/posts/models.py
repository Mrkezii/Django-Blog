from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	update = models.DateTimeField(auto_now=True, auto_now_add=False)  #meaning the everytime saved into db this will be set
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)   #meaning will save when added to DB, will be saved one time



	def __unicode__(self):  #for Python 2
		return self.title

	def __str__(self):     #for Python 3
		return self.title