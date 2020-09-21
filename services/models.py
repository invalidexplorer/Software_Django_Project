from django.db import models
from django.shortcuts import reverse
from accounts.models import CustomUser


class ServicesProduct(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    image1 = models.ImageField(upload_to='ServicesMedia',null=True,blank=True)
    image2 = models.ImageField(upload_to='ServicesMedia',null=True,blank=True)
    image3 = models.ImageField(upload_to='ServicesMedia',null=True,blank=True)
    image4 = models.ImageField(upload_to='ServicesMedia',null=True,blank=True)
    image5 = models.ImageField(upload_to='ServicesMedia',null=True,blank=True)
    description = models.CharField(max_length=100,default='')
    price_range =models.CharField(max_length=100,default='')

    def get_absolute_url(self):
        return reverse('serv-detail', args=[self.id])

