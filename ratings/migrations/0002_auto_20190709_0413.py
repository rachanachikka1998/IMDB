# Generated by Django 2.2.2 on 2019-07-09 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
