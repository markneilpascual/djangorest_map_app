from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import UserSerializer,GroupSerializer,ConstituencySerializer
from .models import Constituency
from rest_framework.response import Response
from django.urls import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'groups': reverse('group-list', request=request, format=format),
        'constituencies': reverse('constituencies-list', request=request, format=format),
})
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group to be viewed or edited.
    """
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
class ConstituencyViewSet(viewsets.ModelViewSet):
    queryset = Constituency.objects.all()
    serializer_class  = ConstituencySerializer