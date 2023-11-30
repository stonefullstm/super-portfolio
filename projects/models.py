from django.db import models


# Profile
class Profile(models.Model):
    name = models.CharField(max_length=100)
    github = models.URLField(max_length=500)
    linkedin = models.URLField(max_length=500)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name


# Project
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    github_url = models.URLField()
    keyword = models.CharField(max_length=50)
    key_skill = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE,
                                related_name="projects")

    def __str__(self):
        return self.name


# CertifyingInstitution
class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.name


# Certificate
class Certificate(models.Model):
    name = models.CharField(max_length=100)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
        default=2
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    profiles = models.ManyToManyField(
        Profile, related_name="certificates", default=2)

    def __str__(self):
        return self.name
