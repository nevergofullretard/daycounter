from datetime import datetime as dt
from django.utils import timezone
from django.utils.timesince import timesince
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as lgin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DateTimeData

from django.contrib.auth.models import User



from .forms import LoginForm


def func_years(from_date, to_date):
    if from_date is None:
        from_date = datetime.now()

    from_date_year = from_date.year
    to_date_year = to_date.year
    diff = from_date_year - to_date_year
    return diff

def func_months(from_date, to_date):
    if from_date is None:
        from_date = datetime.now()

    from_date_year = from_date.month
    to_date_year = to_date.month
    diff = from_date_year - to_date_year
    return diff

@login_required
def home(request):


	now = timezone.now()
	start = DateTimeData.objects.get(id=1).datetime


	years = func_years(from_date=now, to_date=start)

	months_fix = func_months(from_date=now, to_date=start) + years * 12

	months_relative = func_months(from_date=now, to_date=start)


	diff_fix = (now - start)

	hours_fix = diff_fix.days * 24
	min_fix = diff_fix.days * 24 * 60
	sec_fix = diff_fix.days * 24 * 60 * 60




	context = {'now': now, 'start': start, 'diff': diff_fix, 'years': years, 'months_fix': months_fix, 'hours_fix': hours_fix,
	'min_fix': min_fix, 'sec_fix': sec_fix}
	return render(request, 'timer/home.html', context= context)


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			password = form.cleaned_data.get('password')
			print(password)

			try:
				new_login = authenticate(username='admin', password=password)
				lgin(request, new_login)
			except AttributeError:
				pass

		return redirect('/')


	else:
		form = LoginForm()

	context = {'form': form}
	return render(request, 'timer/login.html', context=context)


def add_picture(request):
	return HttpResponse('works')

