from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	class Meta:#gives us space for configurations for a specific model
		model = User #name of the model which would get affected  so form.save would save the data in the User model
		fields = ['username', 'password1']#order of the fields which needs to be shown in the form


	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)
		for fieldname in ['username','password1']:
			self.fields[fieldname].help_text = None