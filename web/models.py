from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Category(models.Model):

    cat_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    user_reg = models.ForeignKey(User, on_delete=models.CASCADE)
    date_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}'.format(self.name)



class Blog(models.Model):

    blog_id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False)
    description = models.TextField(null=False)
    blog_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.author)

    def get_absolute_url(self):
        return '{0}{1}'.format(settings.URL_CUSTOM, self.author)

class Post(models.Model):

    PUBLISHED  = 'PUB'
    EDITION = 'EDI'


    STATUS = (
        (PUBLISHED, 'Published'),
        (EDITION, 'In edit')
    )

    post_id = models.BigAutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False)
    content = models.TextField(null=False)
    image = models.FileField()
    status = models.CharField(max_length=3, choices=STATUS)
    pos_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} {1} {2} ({3})'.format(self.title, self.pos_date, self.author, self.get_status_display())

class Comment(models.Model):

    comment_id = models.BigAutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    com_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1}) ({2})'.format(self.title, self.com_date, self.author)




