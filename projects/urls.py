from rest_framework import routers
from django.urls import path, include
from .views import (CertificateViewSet,
                    CertifyingInstitutionViewSet,
                    ProfileViewSet,
                    ProjectViewSet)

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)
router.register(r"certificates", CertificateViewSet)

urlpatterns = [
  path('', include(router.urls))
]
