# Generated by Django 3.1.6 on 2021-02-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=3)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('num_doc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeSkill', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
