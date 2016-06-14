from django.contrib import admin
from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
class Trade(models.Model):
    tradecode = models.CharField(max_length=200, primary_key=True)	
    bankid = models.CharField(max_length=200, primary_key=True)
    marketserial = models.CharField(max_length=200)
    mktcode = models.CharField(max_length=200, primary_key=True)
