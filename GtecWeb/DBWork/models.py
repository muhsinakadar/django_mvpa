from django.db import models

class Staff(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Position=models.CharField(max_length=30)
    Age=models.IntegerField()

    def __str__(self):
        return self.FirstName+" "+self.LastName

