from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic import ListView
from web.models import *
from web.forms  import *
from django.views.generic.edit import (
    CreateView
)
class BlogListView(ListView):

    model = Blog
    queryset = Blog.objects.all()
    template_name = 'blog/blog_list.html'
    paginate_by = 2

    def get_queryset(self):
        filter_val = self.request.GET.get('filter','')
        new_context = Blog.objects.filter(
            title__contains=filter_val,
        ).order_by('-blog_date')
        return new_context

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter','')
        return context

class BlogDetailView(DetailView):

    model = Blog
    template_name = 'blog/blog_detail.html'

class BlogCreationView(CreateView):

    model = Blog
    template_name = 'blog/blog_form.html'


class PostListView(ListView):

    model = Post
    queryset = Post.objects.all().order_by('-last_modification')
    template_name = 'post/post_list.html'
    paginate_by = 6


class PostListUserView(ListView):

    model = Post
    queryset = Post.objects.all()
    template_name = 'post/post_list.html'
    paginate_by = 3


    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        new_context = Post.objects.filter(
            title__contains=filter_val,author__username=self.kwargs['user']
        ).order_by('-pos_date')
        return new_context

    def get_context_data(self, **kwargs):
        context = super(PostListUserView, self).get_context_data(**kwargs)
        context['user'] = self.kwargs['user']
        context['filter'] = self.request.GET.get('filter', '')
        return context


class postDetailView(DetailView):

    model = Post
    template_name = 'post/post_details.html'

    def get_context_data(self, **kwargs):
        context = super(postDetailView, self).get_context_data(**kwargs)
        if 'model' not in context:
            context['model'] = self.model.objects.filter(author__username=self.kwargs['user'], post_id = self.kwargs['pk'] )
        return context


class postCreationView(CreateView):

    model = Post
    template_name = 'post/post_form.html'
    form_class = PostForm

    @method_decorator(login_required)
    def get(self, request):
        form = PostForm()
        return render(request, 'post/post_form.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):

        blog_id = Blog.objects.get(blog_id=2)
        new_post = Post(author=request.user,blog_id=blog_id)
        form = PostForm(request.POST, request.FILES, instance=new_post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Ad {0} created successfully!'.format(new_post.title))
            welcome_url = request.GET.get('next', 'home')
            return redirect(welcome_url)
        return render(request, 'post/post_form.html', {'form': form})

