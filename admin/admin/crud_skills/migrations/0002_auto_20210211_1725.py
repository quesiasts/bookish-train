# Generated by Django 3.1.6 on 2021-02-11 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_skills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='num_doc',
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.CharField(max_length=5),
        ),
    ]