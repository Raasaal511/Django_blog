from django.urls import path
from . import views


urlpatterns = [
	path('', views.PostList.as_view(), name='post_list'),
	path('post_detail/<str:slug>/', views.ViewPost.as_view(), name='post_detail')

]