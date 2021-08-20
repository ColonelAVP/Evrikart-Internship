from rest_framework import viewsets
from . import models
from . import serializer


class StoreViewset(viewsets.ModelViewSet):
    queryset = models.Store.objects.all()
    serializer_class = serializer.StoreSerializer
