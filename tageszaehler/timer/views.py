
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as lgin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DateTimeData

from .forms import LoginForm

@login_required
def home(request):

	now = timezone.now()
	start = DateTimeData.objects.get(id=1).datetime
	print(start)
	
	print(now)
	diff = now - start



	context = {'now': now, 'start': start, 'diff': diff}
	return render(request, 'timer/home.html', context= context)


def login(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				password = form.cleaned_data.get('password')
				print(password)
				
				new_login = authenticate(username='admin', password=password)
				lgin(request, new_login)
				return redirect('/')
				
				
		else:
			form = LoginForm()

		context = {'form': form}
		return render(request, 'timer/login.html', context=context)


def add_picture(request):
	return HttpResponse('works')

