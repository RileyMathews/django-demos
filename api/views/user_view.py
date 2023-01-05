from rest_framework import viewsets
from django.conf import settings
from api.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

class UserViewset(viewsets.ModelViewSet):
    """ viewset for the user model """
    permission_classes= (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        """ method to control the query of the users table
            The view should filter by active users if the url contains the filter
        """
        queryset = settings.AUTH_USER_MODEL.objects.filter(id=self.request.user.id)

        return queryset
