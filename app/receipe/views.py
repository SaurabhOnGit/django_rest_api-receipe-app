
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated

from core.models import Receipe

from receipe import serializers


class ReceipeViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    serializer_class = serializers.ReceipeSerializer
    queryset = Receipe.objects.all()


    def get_queryset(self):
        # return self.queryset.filter(user=self.request.user).order_by('-id')
        return super().get_queryset().filter(user=self.request.user).order_by('-id')