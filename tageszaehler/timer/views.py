from pytz import timezone as tz # für timezone ändern! https://stackoverflow.com/questions/14657173/get-local-timezone-in-django

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
import tageszaehler.settings as settings

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
	settings_time_zone = tz(settings.TIME_ZONE)

	#now = DateTimeData.objects.get(id=2).datetime.astimezone(settings_time_zone)
	now = timezone.now().astimezone(settings_time_zone) # komischerweise bräuchte man hier gar kein "astimezone", nur zur Sicherheit
	start = DateTimeData.objects.get(id=1).datetime.astimezone(settings_time_zone)
	print('start beziehung:')
	print(start)

	years = func_years(from_date=now, to_date=start)

	months_fix = func_months(from_date=now, to_date=start) + years * 12
	months_relative = func_months(from_date=now, to_date=start)

	diff_fix = (now - start)
	#print(diff_fix)
	print('fixe Differenz')
	print(diff_fix)
	diff_split = str(diff_fix).split(',')
	diff_split2 = diff_split[1].split(':')
	#print(diff_split2)
	hours_fix = diff_fix.days * 24 + int(diff_split2[0]) # könnte evtl falsch sein jeden 13. weil wegen timezone!
	min_fix = diff_fix.days * 24 * 60 + int(diff_split2[1])
	sec_fix = diff_fix.days * 24 * 60 * 60 + int(diff_split2[2].split('.')[0])


	if now.day >= 13:
		previous_thirteenth = dt(int(now.year), int(now.month), 13, 0, 0, 0, 000000).astimezone(settings_time_zone)
	else:
		previous_month = int(now.month) - 1
		if previous_month == 0:
			previous_month = 12
		previous_thirteenth = dt(int(now.year), previous_month, 13, 0, 0, 0, 000000).astimezone(settings_time_zone)
	
	
	print('Jetzt:')
	#print(now)
	print(now.date())
	print('Letzer 13ter:')
	#print(previous_thirteenth)
	print(previous_thirteenth.date())

	days_relative = now.date() - previous_thirteenth.date()


	hours_relative = int(diff_split2[0])
	min_relative = int(diff_split2[1])
	sec_relative = int(diff_split2[2].split('.')[0])









	context = {'now': now, 'start': start, 'diff': diff_fix, 'years': years, 'months_fix': months_fix, 'hours_fix': hours_fix,
	'min_fix': min_fix, 'sec_fix': sec_fix,'days_relative': days_relative, 'months_relative': months_relative, 'hours_relative': hours_relative,
	'min_relative': min_relative, 'sec_relative': sec_relative}
	return render(request, 'timer/home.html', context= context)


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			password = form.cleaned_data.get('password')

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

