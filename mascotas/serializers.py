from rest_framework import serializers

from .models import Animal, Paciente


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"


class PacienteSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    nombre = serializers.CharField()
    apellido_paterno = serializers.CharField()
    apellido_materno = serializers.CharField()


class PatientWithAnimalSerializer(serializers.ModelSerializer):
    patient = PacienteSerializer(read_only=True)

    class Meta:
        model = Animal
        fields = [
            "animal_id",
            "nombre",
            "raza",
            "sexo",
            "pais_origen",
            "color",
            "patient",
        ]
