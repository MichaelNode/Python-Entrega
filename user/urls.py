from django.urls import path, include

from user.views import LoginView, Logout, SignInView


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('signin', SignInView.as_view(), name='signin'),

]
