# Generated by Django 4.2.6 on 2023-10-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(blank=True, max_length=300, null=True)),
                ('ecity', models.CharField(blank=True, max_length=300, null=True)),
                ('esalary', models.FloatField(null=True)),
            ],
        ),
    ]