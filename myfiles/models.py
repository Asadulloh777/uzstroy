from django.db import models

# Create your models here.

class Tur(models.Model):
    nomi = models.CharField(max_length=50)
    def __str__(self):
        return self.nomi

class Loyiha(models.Model):
    nomi = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='media')
    narx = models.IntegerField()
    tur = models.ForeignKey(Tur, on_delete=models.CASCADE)
    manzil = models.CharField(max_length=60)
    vaqt = models.DateTimeField(auto_now=True)

class Murojat(models.Model):
    ism = models.CharField(max_length=33)
    fam = models.CharField(max_length=33)
    mail = models.EmailField()
    text = models.TextField()
    vaqt = models.DateTimeField(auto_now=True)
class Murojatbot(models.Model):
    ism = models.CharField(max_length=33)
    fam = models.CharField(max_length=33)
    mail = models.EmailField()
    text = models.TextField()
    vaqt = models.DateTimeField(auto_now=True)


class Obuna(models.Model):
    name = models.CharField(max_length=17)
    pochta = models.EmailField()