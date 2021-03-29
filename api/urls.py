from django.urls import path
from . import views

urlpatterns = [
    path('user', views.template),
    path('address/', views.template),
    path('category/<str:id>', views.categoryController),
    path('category', views.categoryController),
    path('subCategory', views.template),
    path('item', views.template),
]
