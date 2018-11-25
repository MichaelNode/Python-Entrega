from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
from web.models import Blog, Post,Category
from api.serializers_user import UserListSerializer, UserSerializer, BlogListSerializer,PostListSerializer,PostSerializer
from api.permissions import UserPermission,PostPermission



class UsersListApi(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return  Response(serializer.data, status=status.HTTP_201_CREATED)

class UsersDetailApi(APIView):

    permission_classes = [UserPermission]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request,pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



class BlogViewSet(ModelViewSet):


    queryset = Blog.objects.all()
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['author']
    ordering = ['title']
    filter_fields = ['author__username']


    def get_queryset(self):
        return self.queryset

    def get_serializer_class(self):
        return BlogListSerializer


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, PostPermission]
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    ordering = ['last_modification','title']
    filter_fields = ['title', 'content']

    def get_queryset(self):

        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return self.queryset.order_by('-pos_date')
            else:
                return self.queryset.filter(blog_id__author=self.request.user).order_by('-pos_date')
        return self.queryset.filter(status=Post.PUBLISHED).order_by('-pos_date')

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()

    @action(detail=False)
    def me(self, request):
        posts = Post.objects.filter(author=request.user)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)



class PostDetailApi(APIView):


    permission_classes = [IsAuthenticatedOrReadOnly, PostPermission]

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        return Response(serializer.data)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





