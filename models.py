# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Kart(models.Model):
	kart_id = models.CharField(max_length=100)
	display_name = models.CharField(max_length=100)
	price = models.FloatField()
	ip_address = models.CharField(max_length=36)

class User(models.Model):
	user_id = models.CharField(max_length=100)
	display_name = models.CharField(max_length=100)
	phoneNumber = models.FloatField()
	otp_verified = models.BooleanField(default=False,blank=True)
	otp = models.FloatField(blank=True)
	refresh_token = models.CharField(max_length=100,blank=True) 

class ShoppingExperience(models.Model):
	user_id = models.CharField(max_length=100)
	shopping_id = models.CharField(max_length=100)
	ent_time = models.IntegerField()
	ent_key = models.CharField(max_length=100)
	ent_weight = models.FloatField()
class KartItems(models.Model):
	kart_id = models.ForeignKey(ShoppingExperience,on_delete=models.CASCADE)
	weight = models.FloatField()
	price = models.FloatField()

