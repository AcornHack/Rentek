from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
	address = models.CharField(max_length=100)
	credit_number = models.CharField(max_length=100)
	security_code = models.CharField(max_length=100)
	expiry_date = models.CharField(max_length=100)
	card_type = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100)

	@classmethod
	def create(cls,address,credit_number,security_code,expiry_date,card_type,phone_number):
		customuser = cls(address=address,credit_number=credit_number,security_code=security_code,expiry_date=expiry_date,card_type=card_type,phone_number=phone_number)
		customuser.save()
		return(customuser)

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	body = models.TextField(default= "Hello, I'm a new user.")

	def __str__(self):
		return("Profile of "+self.user.username)

	@classmethod
	def create(cls,user):
		profile = cls(user=user)
		profile.save()
		return(profile)