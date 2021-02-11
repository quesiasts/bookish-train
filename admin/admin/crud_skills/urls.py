from django.urls import include, path
from rest_framework import routers
from .views import SkillsViewSet, PersonViewSet


router = routers.DefaultRouter()
router.register(r'skills',SkillsViewSet, basename="skills")
router.register(r'persons', PersonViewSet, basename="persons")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
