from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    cosname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50) 
    state = models.CharField(max_length=50, null=True) 
    country = models.CharField(max_length=50) 
    zipcode = models.CharField(max_length=50) 

    def __str__(self):
        return(f"{self.cosname}")
