from django.urls import path, include
from web.views import *

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('blogs', BlogListView.as_view(), name='blogs'),
    path('blogs/<user>', PostListUserView.as_view(), name='post-list'),
    path('blogs/<user>/<int:pk>', postDetailView.as_view(), name='post-details'),
    path('new-post', postCreationView.as_view(), name='new-post')
]

