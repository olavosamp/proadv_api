# Generated by Django 3.2 on 2021-04-16 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='terms',
            field=models.ManyToManyField(related_name='publications', to='api.SearchTerm'),
        ),
    ]
