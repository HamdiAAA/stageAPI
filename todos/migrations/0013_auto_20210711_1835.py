# Generated by Django 3.2.4 on 2021-07-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0012_asktobeadmin_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asktobeadmin',
            name='answer',
        ),
        migrations.AddField(
            model_name='asktobeadmin',
            name='discreption',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
