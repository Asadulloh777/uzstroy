# Generated by Django 4.0.5 on 2022-06-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='murojat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=33)),
                ('fam', models.CharField(max_length=33)),
                ('mail', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('vaqt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
