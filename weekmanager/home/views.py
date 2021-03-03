from django.shortcuts import render
from .models import Day
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse


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

    return render(request, 'home/index.html', {'days': days})




