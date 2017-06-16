from django.db import models

# Create your models here.

from django.utils import timezone

class Translation(models.Model):
	translation = models.TextField()
	
	def __str__(self):
		return self.translation
	
class Classifier(models.Model):
	classifier = models.CharField(max_length=100)
	
	def __str__(self):
		return self.classifier
		
class Pinyin(models.Model):
	pinyin = models.CharField(max_length=4)
	pinyin_number_notation = models.CharField(max_length=5)
	
	def __str__(self):
		return self.pinyin
		

class Hanzi(models.Model):
	author = models.ForeignKey('auth.User')
	simplified = models.CharField(max_length=100)
	traditional = models.CharField(max_length=100)
	radicals = models.ManyToManyField('self')
	translations = models.ManyToManyField('Translation')
	classifiers = models.ManyToManyField('Classifier')
	pinyins = models.ManyToManyField('Pinyin')
	stroke_count = models.IntegerField()
	created_date = models.DateTimeField(
            default=timezone.now)
	published_date = models.DateTimeField(
            blank=True, null=True)
			
	def allTranslations(self):
		return ', '.join([str(translation) for translation in self.translations.all()])
		
	def allRadicals(self):
		return ', '.join([str(hanzi) for hanzi in self.radicals.all()])
		
	def allClassifiers(self):
		return ', '.join([str(classifier) for classifier in self.classifiers.all()])
		
	def allPinyins(self):
		return ', '.join([str(pinyin) for pinyin in self.pinyins.all()])
	
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
		