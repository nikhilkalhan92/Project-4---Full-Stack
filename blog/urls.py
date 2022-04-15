from . import views
from django.urls import path



urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('delete_comment/<int:pk>/', views.delete, name='delete_comment'),
    path('update_comment/<int:pk>/', views.update_comment, name='update_comment'),
    
]    
  
    
    

