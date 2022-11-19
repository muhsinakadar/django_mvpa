from django.db import models

class Staff(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Employee(models.Model):
    emp=models.CharField(max_length=30)

    def __str__(self):
        return self.emp
class Student(models.Model):
    name=models.CharField(max_length=40)
    place=models.CharField(max_length=120)
    sclass=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name