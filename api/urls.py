from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import profile

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', profile, name='profile'),
]