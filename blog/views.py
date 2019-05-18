from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #order_by 'date_posted'. '-date_posted' for reverse
    paginate_by = 5


class UserPostListView(ListView):
    # Gets Posts by User
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    # You should use 'object' as context variable in template if you don't provide explictly


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # CreateView expects to have <model>_form.html as template
    # You should use 'object' as context variable in template if you don't provide explictly
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # CreateView expects to have <model>_form.html as template
    # You should use 'object' as context variable in template if you don't provide explictly
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # we are testing if the post is updating or not.
        # we use method 'get_object()' method from 'UpdateView'
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        # we are testing if the post is updating or not.
        # we use method 'get_object()' method from 'UpdateView'
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False


def about(request):
    return render(request, 'blog/about.html')