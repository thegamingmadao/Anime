from django.urls import path

from . import views

app_name = 'anime'

urlpatterns = [
	path('', views.index, name='index'),
	path('r', views.search, name='search'),
	path('<anime_dir>/', views.detail, name='detail'),
	path('<anime_dir>/episode-<episode_number>/', views.episode, name='episode'),
]