from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Subject = models.CharField(max_length=100)
    Message = models.TextField(max_length=250)

    def __str__(self):
        return self.Name


    

