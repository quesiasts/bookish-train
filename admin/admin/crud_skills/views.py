from rest_framework import viewsets
from .serializers import SkillsSerializer, PersonSerializer
from .models import Skills, Person


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all().order_by('typeSkill')
    serializer_class = SkillsSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('full_name')
    serializer_class = PersonSerializer