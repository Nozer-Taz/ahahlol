from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from accounts.views import *


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users-list/', ListUsersView.as_view()),
]
