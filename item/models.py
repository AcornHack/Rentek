from django.db import models
from user.models import CustomUser
from django.contrib.auth.models import User

class item(models.Model):
	name = models.CharField(max_length=100)
	price = models.IntegerField(default=10)
	desc = models.TextField(default= "Hello, I'm a new product.")
	userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

	@classmethod
	def create(cls,name,price,desc,userID):
		customuser = cls(name=name,price=price,desc=desc,userID=userID)
		customuser.save()
		return(customuser)