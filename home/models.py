from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=120, null=True)
    phone = models.CharField(max_length=14, null=True)
    desc = models.TextField(max_length=500, null=True)
    date = models.DateField()

    def __str__(self):
        return self.email
    
