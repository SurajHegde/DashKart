# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import string,random
import datetime
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Kart
from .models import User
from .serializer import KartSerializer
from .serializer import UserSerializer
from .serializer import ShoppingExperienceSerializer
# Create your views here.
def generateOTP(stringLength=6):
	characters = string.ascii_letters + string.digits
	return ''.join(random.choice(characters) for i in range(stringLength))
	
class KartView(APIView):
	def get(self,request):
		karts = Kart.objects.all()
		serializer = KartSerializer(karts,many=True)
		return Response({"Karts" : serializer.data})

class UserView(APIView):
	def post(self,request):		
		phone = request.data.get("phoneNumber")		
		serializer = UserSerializer(data=request.data)
		return Response({"Phone":phone})

class OTPView(APIView):
	def post(self,request):
		phone = request.data.get("phoneNumber")	
		#user_id = request.data.get("user_id")
		#display_name = request.data.get("display_name")
		#print "{} {} {}".format(phone,user_id,display_name)
		'''new_user = User.objects.get(phone_number=phone)
		if new_user.exists():
			print User.objects.get(user_id)
		else:
			User.'''
		otp = generateOTP(6)
		serializers = UserSerializer(data=request.data)
		return Response({"Result":"success","Message":"OTPSent"})

class TokenView(APIView):
	def get(self,request):
		token = random.random() * 10
		return Response({"Token":token})


class EntryView(APIView):
	def get(self,request):
		shopping_id = random.random()
		ent_key = random.random()
		ent_time = datetime.datetime.now()
		return Response({"ID":shopping_id,"Key":ent_key,"Time":ent_time})

class AuthView(APIView):
	def post(self,request):
		shopping_id = request.data.get("shopping_id")
		ent_key = request.data.get("ent_key")
		return Response({"ID":shopping_id})
