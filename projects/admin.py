from .models import Certificate, CertifyingInstitution, Profile, Project
from django.contrib import admin

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(CertifyingInstitution)
admin.site.register(Certificate)
