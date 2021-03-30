from django.urls import path
from . import views

urlpatterns = [
    path('category/<str:id>', views.categoryController),
    path('category', views.categoryController),
    path('subCategory/<str:id>', views.subCategoryController),
    path('subCategory', views.subCategoryController),
    path('item/<str:id>', views.itemController),
    path('item', views.itemController),
]
