
from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers
from django.utils.translation import gettext as _

from core.models import Receipe


class ReceipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receipe

        fields = [
            'id',
            'title',
            'time_minutes',
            'price',
            'link',
        ]


        read_only_fields = ['id']

