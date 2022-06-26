from django.urls import path
from .views import (PostCreateView,
    PostDetailView,
    PostListView,
    PostUpdateView, 
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/new/', PostCreateView.as_view(), name='create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]