from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    national_animal = models.CharField(max_length=255)


class Province(models.Model):
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class City(models.Model):
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    province = models.ForeignKey(Province, on_delete=models.CASCADE)


class Residence(models.Model):
    address = models.CharField(max_length=255)
    year_built = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
