from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

from django.utils.encoding import force_text
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

import json
from .models import CuisineSuggester

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CuisinePopularity(APIView):
    def get(self, request):
        cuisine_list = CuisineSuggester().suggest()
        return Response({
            "suggested_cuisine": cuisine_list
        })
