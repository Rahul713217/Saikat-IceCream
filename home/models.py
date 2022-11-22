from django.db import models

# Create your models here.
'''
makemigrations - create changes and store in a file

migrate - apply the pending changes created by migrations.

'''

class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    # password = models.CharField(max_length=22)
    desc = models.TextField()
    file = models.FileField()
    date = models.DateField()

    def __str__(self):
        return self.name


