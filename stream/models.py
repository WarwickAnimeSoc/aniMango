import datetime

from django.db import models
from django.utils import timezone


class ViewCounter(models.Model):
    name = models.CharField(max_length=10)

    def prune(self):
        to_delete = []
        for view in self.view_set.filter():
            time_since_update = timezone.now() - view.last_update
            print('{0} - Since {1}'.format(view.token, time_since_update))
            if time_since_update > datetime.timedelta(minutes=1):
                to_delete.append(view)

        for view in to_delete:
            view.delete()

    def count(self):
        return str(self.view_set.count())


class View(models.Model):
    counter = models.ForeignKey(ViewCounter, on_delete=models.CASCADE)
    token = models.CharField(max_length=20)
    last_update = models.DateTimeField()


