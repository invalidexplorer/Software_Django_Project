# Generated by Django 2.1.4 on 2019-03-02 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesproduct',
            name='price_range',
            field=models.CharField(default='', max_length=100),
        ),
    ]
