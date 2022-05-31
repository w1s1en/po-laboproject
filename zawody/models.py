from django.db import models

# Create your models here.
class Competition(models.Model):
    nazwa=models.CharField(max_length=999)
    miejsce=models.CharField(max_length=999)
    opis_trasy=models.TextField(max_length=999)
    dystans=models.DecimalField(decimal_places=2,max_digits=5)
    def __str__(self):
        return f'{self.nazwa}'
class Player(models.Model):
    Imie=models.CharField(max_length=999)
    Nazwisko=models.CharField(max_length=999)
    Klub=models.CharField(max_length=999)
    Wiek=models.IntegerField(default=0)
    def __str__(self):
        return f'{self.Imie} {self.Nazwisko}'