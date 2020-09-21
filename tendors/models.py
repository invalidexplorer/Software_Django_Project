from django.db import models
from django.urls import reverse


class Tendorsmod(models.Model):
    requirements = models.CharField(max_length=200,default='')
    author = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
    body = models.TextField(default='')
    description_pdf = models.FileField(upload_to='tendorspdf')
    quantity = models.IntegerField(default=0)
    def __str__(self):

        return self.requirements

class Applypdf(models.Model):
    apply = models.FileField(upload_to='applyfile')
    reciever = models.ForeignKey('Tendorsmod',on_delete=models.CASCADE)
    applier = models.ForeignKey('accounts.CustomUser',on_delete=models.CASCADE)
