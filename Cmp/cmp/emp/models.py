from django.db import models

# Create your models here.


class Student(models.Model):
    Sname = models.CharField(max_length=50)
    Semail = models.EmailField(max_length=254)
    Spassword = models.CharField(max_length=50)
    Saddress = models.TextField()

    def __str__(self) -> str:
        return self.Sname
