# Generated by Django 4.2.1 on 2023-05-29 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Bulletin', '0002_delete_replies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textreply', models.TextField(default='reply')),
                ('replyfrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('replyto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bulletin.post')),
            ],
        ),
    ]