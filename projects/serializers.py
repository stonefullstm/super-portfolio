from rest_framework import serializers
from .models import Certificate, CertifyingInstitution, Profile, Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = ["id", "name", "github", "linkedin", "bio"]
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = ["id", "name", "description",
        # "github_url", "keyword", "key_skill", "profile"]
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        # fields = ["id", "name", "certifying_institution",
        #           "timestamp", "profiles"]
        fields = '__all__'


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        # fields = ("id", "name", "url", "certificates")
        fields = '__all__'

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates")
        institution = CertifyingInstitution.objects.create(**validated_data)

        for certificate_data in certificates_data:
            Certificate.objects.create(
                certifying_institution=institution,
                **certificate_data
            )

        return institution
