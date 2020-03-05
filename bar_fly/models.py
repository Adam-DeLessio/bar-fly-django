from django.db import models
from django.contrib.postgres.fields import ArrayField

class Ingredient(models.Model):
	name = models.CharField(max_length=150)

	def __str__(self):
		return self.name

class Recipe(models.Model):
	name = models.CharField(max_length=160)
	ingredients = ArrayField(models.CharField(max_length=120, blank=True))
	process = models.TextField(null=False)

	def __str__(self):
		return self.name
		
