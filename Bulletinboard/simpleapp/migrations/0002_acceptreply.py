# Generated by Django 4.2.1 on 2023-05-30 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.replies')),
            ],
        ),
    ]
