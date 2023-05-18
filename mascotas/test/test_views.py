import pytest
from django.urls import reverse

from mascotas.models import Animal
from mascotas.serializers import AnimalSerializer


# Views
@pytest.mark.django_db
def test_get_list_animal(client):
    url = reverse("mascotas:animal-list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_animal(client):
    data = {
        "animal_id": "2",
        "nombre": "juan",
        "raza": "beagle",
        "sexo": "M",
        "pais_origen": "Chile",
        "color": "gris",
        "paciente": "0fba2e42-119f-11e6-bcd6-0aa8df4dfcf7",
    }
    url = reverse("mascotas:animal-create")
    response = client.post(url, data=data)
    assert response.status_code == 201
    animal = Animal.objects.first()
    assert animal is not None


@pytest.mark.django_db
def test_detail_animal(client):
    animal = Animal.objects.create(
        animal_id="1",
        nombre="Gato",
        raza="Persa",
        sexo="M",
        pais_origen="Chile",
        color="Blanco",
        paciente="123",
    )
    url = reverse("mascotas:animal-detail", kwargs={"pk": animal.pk})

    response = client.get(url)
    assert response.status_code == 200
    assert response.data["animal_id"] == "1"


# Serializer
@pytest.fixture
def animal_data():
    return [
        {
            "animal_id": "1",
            "nombre": "Gato",
            "raza": "Persa",
            "sexo": "M",
            "pais_origen": "España",
            "color": "Blanco",
            "paciente": "123",
        },
        {
            "animal_id": "2",
            "nombre": "Perro",
            "raza": "Labrador",
            "sexo": "M",
            "pais_origen": "Estados Unidos",
            "color": "Negro",
            "paciente": "456",
        },
    ]


@pytest.fixture
def animal_serializer():
    return AnimalSerializer()


def test_animal_serializer(animal_data, animal_serializer):
    for data in animal_data:
        serialized_data = animal_serializer.validate(data)
        assert isinstance(serialized_data, dict)
        assert "nombre" in serialized_data
        assert "raza" in serialized_data
