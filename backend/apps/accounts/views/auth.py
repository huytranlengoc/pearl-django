from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        refresh_token = response.data['refresh']
        access_token = response.data["access"]
        
        response.delete_cookie('refresh_token')
        response.delete_cookie('access_token')

        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        response.set_cookie(key="access_token", value=access_token, httponly=True)
        return response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data["access_token"]
        response.set_cookie(key="access_token", value=access_token, httponly=True)
        return response
