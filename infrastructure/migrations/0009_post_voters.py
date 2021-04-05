# Generated by Django 3.1.7 on 2021-04-04 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0008_auto_20210404_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='voters',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_of_voted_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
