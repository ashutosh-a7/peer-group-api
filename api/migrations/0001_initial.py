<<<<<<< HEAD
# Generated by Django 3.0.8 on 2020-08-06 14:03

from django.conf import settings
=======
# Generated by Django 3.0.8 on 2020-08-10 16:59

>>>>>>> aa-master
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> aa-master
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_Url', models.CharField(default=False, max_length=200)),
                ('meeting_Time', models.DateTimeField()),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
=======
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=200)),
                ('remarks', models.CharField(max_length=200)),
>>>>>>> aa-master
            ],
        ),
    ]
