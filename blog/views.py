
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = 'blogs'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_create.html'
    fields = ['name', 'description', 'image']
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

@login_required
def like_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    user = request.user
    if user in blog.likes.all():
        blog.likes.remove(user)
    else:
        blog.likes.add(user)
    return redirect('blog:blog_detail', pk=pk)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_list')
    else:
        form = UserCreationForm()
    return render(request, 'login_register.html', {'register_form': form, 'login_form': AuthenticationForm()})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:blog_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login_register.html', {'login_form': form, 'register_form': UserCreationForm()})

def logout_view(request):
    logout(request)
    return redirect('blog:blog_list')
# Create your views here.
