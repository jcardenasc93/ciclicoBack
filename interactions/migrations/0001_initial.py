# Generated by Django 3.0 on 2020-10-28 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150, unique=True)),
                ('edition', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=80)),
                ('website', models.URLField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=80)),
                ('start_latitude', models.CharField(max_length=100)),
                ('start_longitude', models.CharField(max_length=100)),
                ('end_latitude', models.CharField(max_length=100)),
                ('end_longitude', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interactions.AppUser', verbose_name='route_user')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location_latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('location_longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField(blank=True, null=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interactions.Club', verbose_name='event_club')),
            ],
        ),
        migrations.CreateModel(
            name='ClubAppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='interactions.AppUser', to_field='email')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='interactions.Club')),
            ],
            options={
                'unique_together': {('club', 'app_user')},
            },
        ),
        migrations.AddField(
            model_name='appuser',
            name='user_club',
            field=models.ManyToManyField(blank=True, null=True, through='interactions.ClubAppUser', to='interactions.Club'),
        ),
    ]
