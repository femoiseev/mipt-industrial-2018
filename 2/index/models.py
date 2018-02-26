from django.db import models
from django.utils import timezone

class td_item(models.Model):
    item = models.CharField(max_length=20)
    complete = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '<Item: {}, ID: {}>'.format(self.item, self.id)