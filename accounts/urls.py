from django.urls import path
from .views import RegisterView, LoginView, LogoutView, DashBoardView, AccountLockedView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('dashboard', DashBoardView.as_view(), name='dashboard'),
    path('account-locked', AccountLockedView.as_view(), name='account-locked')
]