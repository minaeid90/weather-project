from django.db import models

class Weather(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return str(self.id)
