from django.shortcuts import render
from .models import Day
from django.utils import timezone
from datetime import timedelta
from django.http import  HttpResponse


def index(request):
    """
    days number limit is 7 to represent a whole week
    """
    days_number_limit = 7

    """
    free_spots tells how many days can be added

    now check if any days exist at all, if first day does not exists (so no day does)
    set free_spots to 7
    """
    if not Day.objects.first():
        free_spots = days_number_limit
    else:
        """
        if any day exists free_spots has to be calculated
        how to calculate: take 7 full spots then substract number of days
        that havent come yet during this 7-day period  
        """
        free_spots = days_number_limit - Day.objects.order_by('date').filter(date__gte=timezone.now()).count()

        """
        substract one to avoid duplicating first day during refreshing page
        it is a result of date__gte also taking hours/minutes/second under consideration
        so it is needed to check only day numbers, if they match it means it is the same day
        and there is no 1 free spot for an extra one 
        """
        free_spots = free_spots - 1 if timezone.now().day == Day.objects.first().date.day else free_spots


    """
    now add <free_spots> number of days to fill all the spots and order by date
    """
    for i in range(free_spots):
        day = Day(date=timezone.now() + timedelta(days=i))
        day.save()
    days = Day.objects.all().order_by('date')


    return render(request, 'home/index.html', {'days': days})


