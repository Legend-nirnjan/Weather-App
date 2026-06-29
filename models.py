from django.db import models

# Create your models here.
class Weather(models.Model):
    city=models.CharField(max_length=100)
    temperature=models.FloatField()
    description=models.CharField(max_length=50)
    humidity=models.IntegerField()
    wind_speed=models.FloatField()
    fetched_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.city