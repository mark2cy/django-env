# Generated by Django 2.2.4 on 2019-08-09 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=1000)),
                ('dept_desc', models.CharField(max_length=1000)),
            ],
            options={
                'unique_together': {('dept_name',)},
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_mobile', models.CharField(max_length=100)),
                ('emp_salary', models.IntegerField()),
                ('emp_onboard_date', models.DateTimeField(auto_now=True)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept_emp.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('emp_mobile',)},
            },
        ),
    ]
