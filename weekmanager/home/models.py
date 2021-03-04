from django.db import models
from calendar import day_name

def front_zero(digit):
    return digit if digit > 9 else '0' + str(digit)

class Day(models.Model):
    date = models.DateTimeField()

    def __str__(self):
        weekday = day_name[self.date.weekday()]
        day = front_zero(self.date.day)
        month = front_zero(self.date.month)
        year = self.date.year

        return f'{weekday}, {day}/{month}/{year}'


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.name}'


class Activity(models.Model):
    title = models.CharField(max_length=255, null=False)
    time_start = models.TimeField(null=True)
    time_end = models.TimeField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title} {front_zero(self.time_start.hour)}:{front_zero(self.time_start.minute)} ' \
        f' - {front_zero(self.time_end.hour)}:{front_zero(self.time_end.minute)}'
