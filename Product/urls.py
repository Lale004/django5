from django.urls import path
from . import views
urlpatterns =[
    path('',views.home),
    path('products',views.product_list,name='products'),
    path('product/<int:id>',views.product,name='product' ),
    path('product_create',views.product_create,name='product_create')
]