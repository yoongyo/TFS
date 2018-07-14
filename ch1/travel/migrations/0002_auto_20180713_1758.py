# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfTour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='interest',
            new_name='Duration',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='language',
            new_name='HashTag',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='local',
        ),
        migrations.RemoveField(
            model_name='post',
            name='visited_country',
        ),
        migrations.AddField(
            model_name='post',
            name='BreifContent',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='CourseName',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Created_at',
            field=models.DateTimeField(auto_now_add=True, default='2019-11-11 11:11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='DetailContent',
            field=models.CharField(default='', max_length=1200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Direction',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='GuestInfo',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Map',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Maximum',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='MeetingPoint',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='MeetingTime',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Minimum',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='NotDate',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Price',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Price_include',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='city',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Country'),
        ),
        migrations.AddField(
            model_name='post',
            name='City',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='travel.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Country',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='travel.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Language',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='travel.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Tourtype',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='travel.TypeOfTour'),
            preserve_default=False,
        ),
    ]