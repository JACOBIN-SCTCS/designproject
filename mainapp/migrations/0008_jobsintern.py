# Generated by Django 2.1.1 on 2018-12-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20181227_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobsIntern',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_desc', models.CharField(default='', max_length=40)),
                ('apply_by', models.DateField(blank=True)),
                ('requirements', models.TextField(default='')),
            ],
        ),
    ]
