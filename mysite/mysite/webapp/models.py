from __future__ import unicode_literals

from django.db import models

from datetime import datetime as dt

# Create your models here.

class Diagnosis(models.Model):
	disease = models.CharField(max_length=100)
	user_id = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.disease+" *** "+self.user_id