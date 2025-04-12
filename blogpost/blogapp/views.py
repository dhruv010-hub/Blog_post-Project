from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        return Post.objects.all()

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
