# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=128)),
                ('street', models.CharField(max_length=128)),
                ('house_number', models.IntegerField()),
                ('apt_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adr_email', models.EmailField(max_length=128)),
                ('type', models.IntegerField(choices=[(1, 'domowy'), (2, 'służbowy'), (3, 'komórkowy')])),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=128)),
                ('type', models.IntegerField(choices=[(1, 'domowy'), (2, 'służbowy'), (3, 'komórkowy')])),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_box.Person')),
            ],
        ),
        migrations.AddField(
            model_name='email',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_box.Person'),
        ),
        migrations.AddField(
            model_name='adress',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_box.Person'),
        ),
    ]
