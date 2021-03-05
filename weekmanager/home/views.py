from django.shortcuts import render, redirect, get_object_or_404
from .models import Day, Activity, Category
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import ActivityForm
from django.urls import reverse
from django.contrib import messages

def index(request):
    """
    remove the past days
    filter and order descending 
    if all 7 days passed change nothing, but if there is at least one, exclude it from deleting
    """
    past_days = Day.objects.filter(date__lt=timezone.now()).order_by('-date') # [1:]
    past_days = past_days if past_days.count() == 7 else past_days[1:]

    for d in past_days:
        d.delete()


    if not Day.objects.count():
        """
        if there is no days, take today as the current last day
        free_slots are 7 minus this one day 
        """
        last_day = Day(date=timezone.now())
        last_day.save()
        free_slots = 6
    else:
        """
        get the last day, 
        free slots is just 7 minus nthe number of existing days
        """
        last_day = Day.objects.order_by('date').last()
        free_slots = 7 - Day.objects.count()


    """
    add bonus days up to 7
    timedelta(days=i+1) to avoid adding today's day which has been added at the beginning
    """
    for i in range(free_slots):
        new_day = Day(date=last_day.date + timedelta(days=i+1))
        new_day.save()
    
    days = Day.objects.all()
    categories = Category.objects.all()

    return render(request, 'home/index.html', {'days': days, 'categories': categories})


@require_http_methods(['POST'])
def create(request):
    activity = read_activity_form(request)

    if activity:
        activity.save()
    else:
        messages.error(request, 'Invalid input.')
        
    return redirect(reverse('home:index'))


def delete(request, activity_id):
    activity_to_delete = get_object_or_404(Activity, pk=activity_id)
    activity_to_delete.delete()

    return redirect(reverse('home:index'))


def update(request):
    return HttpResponse('U_P_D_A_T_E')
    

def read_activity_form(request):
    activity_form = ActivityForm(request.POST)
    
    if not activity_form.is_valid():
        return None

    title = activity_form.cleaned_data['title']    
    category = Category.objects.get(pk=activity_form.cleaned_data['category'])
    date = Day.objects.get(pk=activity_form.cleaned_data['date'])
    fr0m = activity_form.cleaned_data['fr0m']
    to = activity_form.cleaned_data['to']

    return Activity(title=title, category=category, day=date, time_start=fr0m, time_end=to) \
        if fr0m < to else None
    
    
