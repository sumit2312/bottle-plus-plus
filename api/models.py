from django.db import models

# Create your models here.

class Bottles(models.Model):
    level = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)

class Patients(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bottle = models.ForeignKey(Bottles, on_delete=models.CASCADE)
    disease = models.CharField(max_length=100)
    room_number = models.IntegerField()
    bed_number = models.IntegerField()

    def __str__(self):
        return self.name

class BottleStats(models.Model):
    bottle_primary_key = models.IntegerField()
    level = models.IntegerField()
    timestamp  = models.DateTimeField()
    rate = models.FloatField(null=True, blank=True, default=None)
    estimated_time_left = models.IntegerField(null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        try:
            self.estimated_time_left = int(self.level)/self.rate
        except:
            pass
        return super().save(*args, **kwargs)    

    def __str__(self):
        return str(self.bottle_primary_key)

