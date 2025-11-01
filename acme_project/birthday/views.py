from django.shortcuts import render
from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday
from django.shortcuts import get_object_or_404, render

def birthday(request, pk=None):
    if pk is not None:
        instace = get_object_or_404(Birthday, pk=pk)
    else:
        instace = None

    form = BirthdayForm(request.POST or None, instance=instace)
    
    context = {'form': form}
    if form.is_valid():
        form.save()
        birthday_countdown = calculate_birthday_countdown(form.cleaned_data['birthday'])
        context.update({'birthday_countdown' : birthday_countdown})
    return render(request, 'birthday/birthday.html', context) 



def birthday_list(request):
    birthdays = Birthday.objects.all()
    context = {"birthdays": birthdays}
    return render(request, 'birthday/birthday_list.html', context)
