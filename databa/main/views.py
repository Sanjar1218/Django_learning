from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'pages/post_delete.html'
    
    def test_func(self):
        return self.request.user == self.get_object().author

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'pages/post_create.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'pages/post_create.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author
    
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # print(context['posts'][0].author.profile)
    return render(request, 'pages/home.html', context=context)

def about(request):
    return render(request, 'pages/about.html')