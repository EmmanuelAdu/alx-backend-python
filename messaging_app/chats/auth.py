from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Custom Serializer
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


class CustomTokenRefreshView(TokenRefreshView):
    pass