from tkinter import CASCADE
from django import shortcuts
from django.db import models

# Create your models here.
class Competition(models.Model):
    nazwa=models.CharField(max_length=999)
    miejsce=models.CharField(max_length=999)
    opis_trasy=models.TextField(max_length=999)
    dystans=models.DecimalField(decimal_places=2,max_digits=5)
    def __str__(self):
        return f'{self.nazwa}'
    

class Bike(models.Model):
    Model=models.CharField(max_length=999)
    Marka=models.CharField(max_length=999)
    Waga=models.DecimalField(decimal_places=2,max_digits=5)
    def __str__(self):
        return f'{self.Marka} {self.Model}'

class Player(models.Model):
    Imie=models.CharField(max_length=999)
    Nazwisko=models.CharField(max_length=999)
    Klub=models.CharField(max_length=999)
    Wiek=models.IntegerField(default=0)
    rower=models.ForeignKey(Bike,on_delete=models.CASCADE,blank=True, null=True)
    player=models.ManyToManyField(Competition)
    shortcut=models.CharField(max_length=20,default=None)
    def __str__(self):
        return f'{self.Imie} {self.Nazwisko}'