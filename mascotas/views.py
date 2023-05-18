import logging
import uuid

import requests
from rest_framework import generics
from rest_framework.response import Response

from .models import Animal, Paciente
from .serializers import AnimalSerializer, PatientWithAnimalSerializer

logger = logging.getLogger("mascotas")


class AnimalListAPIView(generics.ListAPIView):
    serializer_class = PatientWithAnimalSerializer

    def get_queryset(self):
        return Animal.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            page = self.concat_animals_with_patients(page)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_patients_ids(self, queryset):
        return [animal.paciente for animal in queryset]

    def get_patients(self, page):
        url = f"https://3y1hl3jca0.execute-api.us-east-1.amazonaws.com/pacientes_endpoint?page={page}"
        response = requests.get(url)

        if response.status_code != 200:
            return []
        data = response.json()
        return data["results"]

    def filter_patients_by_ids(self, ids):
        filtered_patients = []
        page = 1
        while True:
            patients = self.get_patients(page)
            filtered_patients.extend(
                patient for patient in patients if patient["uuid"] in ids
            )
            if not patients:
                break

            if patients[-1].get("next_page") is None:
                break

            page += 1

        return filtered_patients

    def concat_animals_with_patients(self, page):
        patients_ids = self.get_patients_ids(page)
        patients = self.filter_patients_by_ids(patients_ids)
        for animal in page:
            for patient in patients:
                if patient["uuid"] == animal.paciente:
                    animal.patient = Paciente(
                        nombre=patient["nombre"],
                        apellido_paterno=patient["apellido_paterno"],
                        apellido_materno=patient["apellido_materno"],
                    )
        return page


class AnimalDetailAPIView(generics.RetrieveAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalCreateAPIView(generics.CreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalPartialUpdateAPIView(generics.UpdateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalDeleteAPIView(generics.DestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
