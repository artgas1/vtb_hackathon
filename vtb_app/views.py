from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import permissions
from .vtb_api import *
from rest_framework.parsers import FileUploadParser


class TestView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        return Response({"Method": "GET"})

    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data.get('text'))
        return Response(serializer.errors)


class CarRecognizeView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    # permission_classes = [permissions.IsAuthenticated]
    # parser_classes = [ImageUploadParser]

    def post(self, request, format=None):
        serializer = CarRecognizeSerializer(data=request.data)
        if serializer.is_valid():
            photo = request.data.get('photo')
            response = car_recognize_method(photo.file.read())
            return Response(response)
        return Response(serializer.errors)
