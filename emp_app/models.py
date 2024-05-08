from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200,null=False)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    
class Role(models.Model):
    name = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.name

    
class Employee(models.Model):
    first_name = models.CharField(max_length=200,null=False)
    last_name = models.CharField(max_length=200)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    add=models.TextField(null=True,blank=True,max_length=200)
    salary = models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()
    img=models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.first_name},{self.dept},{self.role}'