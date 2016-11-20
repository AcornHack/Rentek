from django.db import models
from user.models import CustomUser
from django.contrib.auth.models import User

class item(models.Model):
	name = models.CharField(max_length=100)
	price = models.IntegerField(default=10)
	deposit = models.IntegerField(default=10)
	desc = models.TextField(default= "Hello, I'm a new product.")
	userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

	@classmethod
	def create(cls,name,price,desc,userID,deposit):
		customuser = cls(name=name,price=price,desc=desc,userID=userID,deposit=deposit)
		customuser.save()
		return(customuser)

class rent(models.Model):
	itemID = models.ForeignKey(item, on_delete=models.CASCADE)
	renteeID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	start_date = models.DateField(auto_now=False, auto_now_add=False)
	end_date = models.DateField(auto_now=False, auto_now_add=False)

	@classmethod
	def create(cls,itemID,renteeID,start_date,end_date):
		customuser = cls(itemID=itemID,renteeID=renteeID,start_date=start_date,end_date=end_date)
		customuser.save()
		return(customuser)