from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data["access"]
        response.set_cookie(key="jwt", value=token, httponly=True)
        return response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data["access"]
        response.set_cookie(key="jwt", value=token, httponly=True)
        return response
