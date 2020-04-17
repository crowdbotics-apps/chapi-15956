from rest_framework import authentication
from chapp.models import CHdb
from .serializers import CHdbSerializer
from rest_framework import viewsets


class CHdbViewSet(viewsets.ModelViewSet):
    serializer_class = CHdbSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CHdb.objects.all()
