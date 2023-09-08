from django.shortcuts import render

from rest_framework import viewsets

# Create your views here.
from cpims_api.serializers import RegOrgUnitSerializer
from cpovc_registry.models import RegOrgUnit

class RegOrgUnitViewSet(viewsets.ModelViewSet):
    # queryset = RegOrgUnit.objects.all()
    # serializer_class = RegOrgUnitSerializer
    
      # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the rRegOrgUnit items for given requested user
        '''
        rRegOrgUnits = RegOrgUnit.objects.filter(user = request.user.id)
        serializer = RegOrgUnitSerializer(rRegOrgUnits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    