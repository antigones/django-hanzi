from django.db import models

# Create your models here.

from django.utils import timezone


class Radical(models.Model):
	author = models.ForeignKey('auth.User')
	radical = models.CharField(max_length=1)
	translation = models.TextField()
	pinyin = models.CharField(max_length=4)
	pinyin_number_notation = models.CharField(max_length=5)
	stroke_count = models.IntegerField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.radical
		
class Hanzi(models.Model):
	author = models.ForeignKey('auth.User')
	hanzi = models.CharField(max_length=100)
	hanzi_traditional = models.CharField(max_length=100)
	radicals = models.ManyToManyField(Radical)
	translation = models.TextField()
	pinyin = models.CharField(max_length=4)
	pinyin_number_notation = models.CharField(max_length=5)
	stroke_count = models.IntegerField()
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.hanzi
		
class Test(models.Model):
	name = models.CharField(max_length=100)
	hanzis = models.ManyToManyField(Hanzi)
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name
		