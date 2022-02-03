
from django.urls import path
from userscbi import views

urlpatterns = [
    path('users/', views.UserListAPIview.as_view()),
    path('users/<int:pk>/', views.UserDetailAPIview.as_view()),
]