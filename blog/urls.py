from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/like/', views.like_blog, name='like_blog'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]