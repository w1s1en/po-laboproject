# Generated by Django 4.0.4 on 2022-05-31 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zawodnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imie', models.CharField(max_length=999)),
                ('Nazwisko', models.CharField(max_length=999)),
                ('Klub', models.CharField(max_length=999)),
                ('Wiek', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Zawody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=999)),
                ('miejsce', models.CharField(max_length=999)),
                ('opis_trasy', models.TextField(max_length=999)),
                ('dystans', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
