from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API features"""

        an_APIView = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message' : 'Hello' , 'an_APIView' : an_APIView})

    def post(self, request):
        """Create a hello message with a name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})


    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test a ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, requets):
        """Return a hello message"""

        a_viewset= [
        'Uses actions (list, create, retrieve, update, partial_update)',
        'Automatically maps to URLS using Routers',
        'Provides more functionality with less code',
        ]

        return Response({'message' : 'Hello!' , 'a_viewset' : a_viewset})

    def create(self, request):
        """Create a new hello message"""

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message' : message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'HTTP method' : 'GET'})

    def update(self, request, pk=None):
        """Hanlde updating an object by its ID"""
        return Response({'HTTP method' : 'PUT'})

    def partial_update(self, request, pk=None):
        """Hanlde partially updating an object by its ID"""
        return Response({'HTTP method' : 'PATCH'})

    def destroy(self, request, pk=None):
        """Hanlde deleting an object by its ID"""
        return Response({'HTTP method' : 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email' )


class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
