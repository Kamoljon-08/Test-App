from django.urls import path
from .views import login_view, logout_view, signup_view, update_user, profile
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("update/", update_user, name="update"),
    path("profile/<str:username>/", profile, name="profile"),
    # path("login2/", LoginView.as_view(), name="login2"),
    # path("logout2/", LogoutView.as_view(), name="logout2"),

]
