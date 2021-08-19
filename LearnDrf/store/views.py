# Requirements
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializer import StoreSerializer
from .models import Store


# Create your views here.
class StoreList(APIView):
    """
        1) Get a List of all the stores
        2) Post a store
    """
    serializer_class = StoreSerializer

    def get(self, request):
        stores = Store.objects.all()
        data = StoreSerializer(stores, many=True).data
        return Response(data)

    def post(self, request):
        serializer = StoreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreDetail(APIView):
    """
        1) Get details of a Store
        2) Update information of a Store
        3) Delete information of a Store
    """

    serializer_class = StoreSerializer

    def get(self, request, pk):
        store = get_object_or_404(Store, pk=pk)
        try:
            serializer = StoreSerializer(store)
            data = serializer.data
        except:
            data = status.HTTP_400_BAD_REQUEST
        return Response(data)

    def put(self, request, pk):
        store = get_object_or_404(Store, pk=pk)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        store = get_object_or_404(Store, pk=pk)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
