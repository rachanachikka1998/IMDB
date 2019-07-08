# Generated by Django 2.2.2 on 2019-07-08 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('release_date', models.DateField()),
                ('actors', models.ManyToManyField(related_name='movie_actors', to='ratings.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='MovieRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('no_of_ratings', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='ratings.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieCast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('cast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='casted_in', to='ratings.Actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cast', to='ratings.Movie')),
            ],
        ),
    ]