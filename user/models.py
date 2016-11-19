from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
	address = CharField()
	credit_number = CharField()
	security_code = CharField()
	expiry_date = CharField()
	card_type = CharField()
	phone_number = CharField()

	@classmethod
	def create(cls,address,credit_number,security_code,expiry_date,card_type,phone_number):
		customuser = cls(address=address,credit_number=credit_number,security_code=security_code,expiry_date=expiry_date,card_type=card_type,phone_number=phone_number)
		customuser.save()
		return(customuser)
