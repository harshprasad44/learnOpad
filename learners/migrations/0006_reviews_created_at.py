# Generated by Django 3.0.7 on 2020-08-28 18:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learners', '0005_auto_20200828_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
