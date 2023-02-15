from apps.accounts.serializers import UserSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


class UserView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
