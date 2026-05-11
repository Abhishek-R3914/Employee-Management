from django.db import models

Status_Choices = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200, unique=True)
    department = models.CharField(max_length=200)
    salary = models.IntegerField()
    status = models.CharField(max_length=20, choices=Status_Choices, default='Active')
    
    def __str__(self):
        return self.name