# Generated by Django 3.2.7 on 2021-11-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20211125_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='ouvinte',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=249, null=True),
        ),
    ]
