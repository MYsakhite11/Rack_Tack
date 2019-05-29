from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

User = get_user_model()

#create the form class.
class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['name_task', 'description','begin_time', 'end_time']
		widgets = {
			'name_task': forms.TextInput(
				attrs={
					'class': 'form-control', 'placeholder': 'Entrer le nom de la tache'
				}
				),
			'description': forms.Textarea(
				attrs={
					'class': 'form-control', 'placeholder': 'Entrer la description'
				}
				),
			'begin_time': forms.DateInput(
				attrs={
					'class': 'form-control', 'placeholder': 'Date de debut'
				}
				),
			'end_time': forms.DateInput(
				attrs={
					'class': 'form-control', 'placeholder': 'Date de fin'
				}
				)
		}


class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={
					'class': 'form-control', 'placeholder': 'Username'
				}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={
					'class': 'form-control', 'placeholder': 'Mot de passe'
				}))

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("L'utilisateur n'existe pas !")

			if not user.check_password(password):
				raise forms.ValidationError("Mot de passe incorrecte !")

			if not user.is_active:
				raise forms.ValidationError("L'utilisateur n'est pas active !")
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	#email = forms.EmailField()
	Confirmer_Adresse = forms.EmailField(widget=forms.EmailInput(attrs={
					'class': 'form-control', 'placeholder': 'Confirmer_Adresse',
				}))
	class Meta:
		model = User
		fields = ['username', 'email', 'Confirmer_Adresse', 'password']
		widgets = {
		'username': forms.TextInput(
			attrs={
				'class': 'form-control', 'placeholder': "Nom d'utilisateur"
			}
			),
		'email': forms.EmailInput(
			attrs={
				'class': 'form-control', 'placeholder': 'Adresse mail'
			}
			),
		'password': forms.PasswordInput(
			attrs={
				'class': 'form-control', 'placeholder': 'Mot de passe'
			}
			)
		}

	def clean_Confirmer_Adresse(self):
		email = self.cleaned_data.get('email')
		Confirmer_Adresse = self.cleaned_data.get('Confirmer_Adresse')

		if email != Confirmer_Adresse:
			raise forms.ValidationError('Les adresses doivent correspondre')
			print(email != email2)
		emai_exist = User.objects.filter(email=email)
		if emai_exist.exists():
			raise forms.ValidationError('Adresse existe deja')
		return email




















# class UserForm(ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ['user_name', 'first_name', 'last_name', 'password', 'email']
# 		widgets = {
# 			'user_name': forms.TextInput(
# 				attrs={
# 					'class': 'form-control'
# 					}
# 				),
# 			'first_name': forms.TextInput(
# 				attrs={
# 					'class': 'form-control'
# 					}
# 				),
# 			'last_name': forms.TextInput(
# 				attrs={
# 					'class': 'form-control'
# 					}
# 				),
# 			'password': forms.PasswordInput(
# 				attrs={
# 					'class': 'form-control'
# 					}
# 				),
# 			'email': forms.EmailInput(
# 				attrs={
# 					'class': 'form-control'
# 					}
# 				),
# 		}
