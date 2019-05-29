from django.shortcuts import render
from .form import UserLoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import *
from .form import *


# Create your views here.
def accueil(request):

	return render(request, 'base.html')


def saver_task(request):
	form  = TaskForm(data=request.POST)
	
	if(request.method == 'POST'):
		if form.is_valid():
			name_task = form.data['name_task']
			description = form.data['description']
			begin_time = form.data['begin_time']
			end_time = form.data['end_time']
			if(name_task and description and end_time):

				task = Task(name_task=name_task, description=description, begin_time=begin_time, end_time=end_time)
				task.user = request.user
				task.save()
				messages.success(request, "Enregistrement reussi")
				return render(request, 'aft.html')

	context = {
		'form': form
	}
	messages.error(request, "Enregistrement non reussi")
	return render(request, 'register_task.html', context)


def list(request):
	
	queryset = Task.objects.all()
	
	query = request.GET.get('search')
	if query:
		queryset = queryset.filter(
			Q(name_task=query) |
			Q(description=query)
			).distinct()

	context = {
		'obj_list': queryset,
		}

	return render(request, 'task_list.html', context)



def delete_task(request, id=None, template_name='register_task.html'):
	instance = get_object_or_404(Task, id=id)

	instance.delete()
	messages.success(request, "Suppression reussi")
	return redirect('racktack_app:list')
	


def update_task(request, id=None, template_name='register_task.html'):
	instance = get_object_or_404(Task, id=id)
	form = TaskForm(data=request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Mise à jour reussi!")
		return redirect('racktack_app:list')

	context={
		'task_name': instance.name_task,
		'insstance': instance,
		'form': form,  
	}
	messages.error(request, "Mise à jour non reussi")
	return render(request, template_name, {'form': form})


def aft(request):

	return render(request, 'aft.html')

def login_view(request):
	title = "Login"
	form = UserLoginForm(data=request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('racktack_app:list')

	return render(request, 'login.html', {'form': form, 'title': title})


def detail(request, id):
	instance = get_object_or_404(Task, id=id)
	form = TaskForm(data=request.POST or None, instance=instance)

	context = {
		'form': form
	}
	
	return render(request, 'detail.html', context)

def register_view(request):
	title = 'Inscription'
	form = UserRegisterForm(data=request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		new_user = authenticate(username=username, password=password)
		login(request, new_user)
		return redirect('racktack_app:saver_task')

	context = {
	'form': form,
	'title': title
	}
	return render(request, 'login.html', context)


def logout_view(request):
	logout(request)
	return redirect('/racktack_app')