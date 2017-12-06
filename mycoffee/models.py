from django.db import models
from django.contrib.auth.models import User

class Bean(models.Model):
	name = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=5, decimal_places=3)

	def __str__(self):
		return self.name

class Roast(models.Model):
	name = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=5, decimal_places=3)

	def __str__(self):
		return self.name

class Syrup(models.Model):
	name = models.CharField(max_length=30) #different kind of syrup
	price = models.DecimalField(max_digits=5, decimal_places=3)

	def __str__(self):
		return self.name

class Powder(models.Model):
	name = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=5, decimal_places=3)

	def __str__(self):
		return self.name

class CoffeeOrder(models.Model):
	user=models.ForeignKey(User)
	name=models.CharField(max_length=100)
	espresso_shots=models.PositiveIntegerField(default=1)
	bean=models.ForeignKey(Bean)
	roast=models.ForeignKey(Roast)
	syrup=models.ManyToManyField(Syrup, blank=True) #why blank=True
	powders=models.ManyToManyField(Powder, blank=True)
	water=models.FloatField()
	steamed_milk=models.BooleanField(default=False)
	foam=models.FloatField()
	extra_instructions=models.TextField(max_length=200)
	price=models.DecimalField(max_digits=6, decimal_places=3, null=True) #why null=True

	def __str__(self):
		return self.name


