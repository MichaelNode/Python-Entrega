from rest_framework import serializers
from django.contrib.auth.models import User

from web.models import *


class BlogListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Blog
        fields = (

            'author',
            'title',
            'description'
        )

class BlogSerializer(BlogListSerializer):

    class Meta(BlogListSerializer.Meta):

        fields = '__all__'
        read_only_fields = ['blog_id']

class PostListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = (
            'blog_id',
            'cat_id',
            'author',
            'title',
            'content',
            'image'
        )






