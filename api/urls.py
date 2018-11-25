from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet,BlogViewSet

router = DefaultRouter()
router.register('post', PostViewSet, base_name='post')
router.register('blogs', BlogViewSet, base_name='blogs')

from api.views import UsersListApi, UsersDetailApi,PostDetailApi

urlpatterns = [
    path('api/1.0/users/', UsersListApi.as_view(), name='users_list'),
    path('api/1.0/users/<int:pk>', UsersDetailApi.as_view(),name='users_details'),
    path('api/1.0/', include(router.urls)),
    path('api/1.0/post/<int:pk>', PostDetailApi.as_view(),name='blogs_options'),
]
