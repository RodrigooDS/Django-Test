from django.db import models


class Animal(models.Model):
    MASCULINO = "M"
    FEMENINO = "F"
    SEXO_CHOICES = [
        (MASCULINO, "Masculino"),
        (FEMENINO, "Femenino"),
    ]

    animal_id = models.CharField(max_length=50, null=False)
    nombre = models.CharField(max_length=100, null=False)
    raza = models.CharField(max_length=100, null=False)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, null=False)
    pais_origen = models.CharField(max_length=100, null=False)
    color = models.CharField(max_length=100, null=False)
    paciente = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"ID: {self.id} - Name: {self.nombre}"


class Paciente(models.Model):
    uuid = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
