# Generated by Django 4.0.6 on 2023-02-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
