# Generated by Django 3.1.7 on 2021-04-01 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0006_auto_20210401_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='infrastructure.post'),
        ),
    ]
