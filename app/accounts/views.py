from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from app.accounts.serializers import MyAuthTokenSerializer


class MyObtainAuthToken(ObtainAuthToken):
    serializer_class = MyAuthTokenSerializer


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def whoiam(request):

    user = request.user
    breakpoint()
    data = {
        "id": user.id,
        "user": user.email,
        "created_at": user.created_at,
        "modified_at": user.modified_at,
        "permission": {
            "ADMIN": user.is_superuser,
            "STAFF": user.is_staff,
        }
    }

    return Response(data)


obtain_auth_token = MyObtainAuthToken.as_view()
