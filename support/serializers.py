"""
    Support Serializers
    Mostafa Rasouli
    Email: mostafarasooli54@gmail.com
    2023/08/26
"""

# Third Party
from rest_framework import serializers
# Local
from . import models


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactForm
        fields = ["creator", "email", "phone_number", "message"]
