# Generated by Django 3.0.8 on 2020-10-05 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_myuser_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.CharField(default='New Student', max_length=256),
            preserve_default=False,
        ),
    ]