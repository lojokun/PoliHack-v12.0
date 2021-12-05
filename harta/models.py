from django.db import models


class Camioane(models.Model):
    nr_matriculare = models.CharField(max_length=7)
    latitudine = models.FloatField(default=45)
    longitudine = models.FloatField(default=25)
    masa_masurata = models.FloatField()


class Lemne(models.Model):
    tipul_lemnului = models.TextField()
    densitate = models.FloatField()


class Aviz(models.Model):
    id_camion = models.ForeignKey(Camioane, on_delete=models.CASCADE)
    data_emiterii = models.DateField()
    data_finalizarii = models.DateTimeField()
    id_lemne = models.ForeignKey(Lemne, on_delete=models.CASCADE)
    volum = models.FloatField()
    masa_calculata = models.FloatField()
