from django.urls import path
from .views import RegisterView, LoginView, GetUserView,GetAllUsersDetails

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('getuser/', GetUserView.as_view(), name='get-user'),
    path('users/',GetAllUsersDetails.as_view())
]
