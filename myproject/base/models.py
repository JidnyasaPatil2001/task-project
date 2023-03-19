from django.db import models

# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    createdby=models.CharField(max_length=200)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.name 

# class User(models.Model):
#      name=models.CharField(max_length=200)
#      created=models.DateTimeField(auto_now_add=True)
#      createdby=models.CharField(max_length=200)

#      def __str__(self):
#           return self.name 