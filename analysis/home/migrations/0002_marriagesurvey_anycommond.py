# Generated by Django 4.1.4 on 2023-12-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marriagesurvey',
            name='anycommond',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
