from django.urls import path

from .views import LoginPageView

urlpatterns = [
    # path("signup/", SignUpView.as_view(), name="signup"),
    path('login/', LoginPageView.as_view(), name='login')
]