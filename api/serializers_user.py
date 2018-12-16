from django.contrib.auth.models import User
from rest_framework import serializers

from web.models import Post, Blog, Category


class UserListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()


class UserSerializer(UserListSerializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = User()
        return self.update(user, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, value):

        if self.instance is not None and self.instance.username != value and User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username {0} already exists'.format(value))

        if self.instance is None and User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username {0} already exists'.format(value))

        return value

class BlogListSerializer(serializers.Serializer):

    blog_id = serializers.ReadOnlyField()
    author = serializers.SerializerMethodField()
    title = serializers.CharField()
    description = serializers.CharField()
    url = serializers.ReadOnlyField(source='get_absolute_url')

    def get_author(self, obj):
        return obj.author.username


class BlogSerializer(BlogListSerializer):

    read_only_fields = ['author']

    def create(self, validated_data):
        blog = Blog()
        return self.update(blog, validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author')
        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description')
        instance.save()
        return instance


class PostListSerializer(serializers.Serializer):

    title = serializers.CharField()
    content = serializers.CharField()
    image = serializers.FileField()
    pos_date = serializers.DateTimeField()


    def get_blog_id(self, obj):
        return obj.blog_id

    def get_cat_id(self, obj):
        return obj.cat_id


class PostSerializer(PostListSerializer):

    blog_id = serializers.CharField()
    cat_id = serializers.CharField()

    read_only_fields = ['author','post_id']

    def create(self, validated_data):
        post = Post()
        return self.update(post, validated_data)

    def update(self, instance, validated_data):

        instance.author = validated_data.get('author')
        instance.blog_id =Blog.objects.get(blog_id=validated_data.get('blog_id'))
        instance.cat_id = Category.objects.get(cat_id=validated_data.get('cat_id'))
        instance.title = validated_data.get('title')
        instance.content = validated_data.get('content')
        instance.image = validated_data.get('image')
        instance.pos_date = validated_data.get('pos_date')
        instance.save()
        return instance





