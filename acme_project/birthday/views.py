from django.shortcuts import render
from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday

def birthday(request):
    form = BirthdayForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(form.cleaned_data['birthday'])
        context.update({'birthday_countdown' : birthday_countdown})
    return render(request, 'birthday/birthday.html', context) 

def birthday_list(request):
    birthdays = Birthday
