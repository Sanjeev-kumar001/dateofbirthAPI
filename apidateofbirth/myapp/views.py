from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer
from datetime import date

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.age = self.calculate_age(instance.date_of_birth)
        instance.save()

    def calculate_age(self, date_of_birth):
        today = date.today()
        age = today.year - date_of_birth.year

        # Check if the birthday has occurred this year
        if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
            age -= 1

        return age
