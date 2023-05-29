from django.urls import path
from . import views
urlpatterns =[
    path('',views.home),
    path('products',views.product_list),
    path('product/<int:id>',views.product)
]