from rest_framework import serializers

class KartSerializer(serializers.Serializer):
	kart_id = serializers.CharField(max_length=100)
	display_name = serializers.CharField(max_length=100)
	ip_address = serializers.CharField(max_length=100)
class UserSerializer(serializers.Serializer):
	user_id = serializers.CharField(max_length=100)
	display_name = serializers.CharField(max_length=100)
	phoneNumber = serializers.FloatField()
	otp = serializers.FloatField()
	otp_verified = serializers.BooleanField()
	refresh_token = serializers.CharField(max_length=100)
class ShoppingExperienceSerializer(serializers.Serializer):
	user_id = serializers.CharField(max_length=100)
	shopping_id = serializers.CharField(max_length=100)
	ent_time = serializers.IntegerField()
	ent_key = serializers.CharField(max_length=100)
	ent_weight = serializers.FloatField()
class KartItemsSerializer(serializers.Serializer):
	weight = serializers.FloatField()
	price = serializers.FloatField()
