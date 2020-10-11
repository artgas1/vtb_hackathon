from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from .vtb_api import *


class TestViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class SearchHistoryViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SearchHistorySerializer
    queryset = SearchHistory.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        SearchHistory.objects.all().delete()
        return Response("Successfully deleted search history")


class LoanHistoryViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LoanHistorySerializer
    queryset = LoanHistory.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        LoanHistory.objects.all().delete()
        return Response("Successfully deleted loan history")


class ExtraUserDataViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExtraUserDataSerializer
    queryset = ExtraUserData.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CarRecognizeViewSet(viewsets.ViewSet):
    serializer_class = CarRecognizeSerializer

    def list(self, request):
        return Response('Car recognize Method')
        pass

    def create(self, request):
        serializer = CarRecognizeSerializer(data=request.data)
        if serializer.is_valid():
            photo = request.data.get('photo')
            response = car_recognize_method(photo)
            if request.auth:
                sh_model = SearchHistory(response=response, user=request.user)
                sh_model.save()
            return Response(response)
        return Response(serializer.errors)


class CarLoanViewSet(viewsets.ViewSet):
    serializer_class = CarLoanSerializer

    def list(self, request):
        return Response('Car loan Method')
        pass

    def create(self, request):
        serializer = CarLoanSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            response = car_loan_method(serializer.data)
            if request.auth:
                if request.auth:
                    lh_model = LoanHistory(response=response, user=request.user)
                    lh_model.save()
            return Response(response)

        return Response(serializer.errors)
