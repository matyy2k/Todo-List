# Generated by Django 3.2.5 on 2021-07-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20210724_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]