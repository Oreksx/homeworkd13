# Generated by Django 4.2.1 on 2023-05-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0002_acceptreply'),
    ]

    operations = [
        migrations.AddField(
            model_name='replies',
            name='isaccepted',
            field=models.BooleanField(default=False),
        ),
    ]
