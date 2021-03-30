from django.urls import path
from . import views

urlpatterns = [
    path('category/<str:id>', views.categoryController),
    path('category', views.categoryController),
    path('subCategory', views.subCategoryController),
    path('item', views.itemController),
]
