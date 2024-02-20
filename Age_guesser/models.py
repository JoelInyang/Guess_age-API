from django.db import models

class AgePrediction(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    #date_of_birth = models.DateField()
    date_of_birth = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
