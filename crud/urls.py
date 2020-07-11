from django.urls import path
from . import views

app_name = 'crud'
urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('book_create/', views.book_create, name='book_create'),
    path('book_update/<int:pk>/', views.book_update, name='book_update'),
    path('book_delete/<int:pk>/', views.book_delete, name='book_delete'),
]
