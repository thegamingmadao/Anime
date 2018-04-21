from django.urls import path

from . import views

app_name = 'anime'

urlpatterns = [
	path('', views.index, name='index'),
	path('r', views.search, name='search'),
	path('test/', views.test),
	path('contact/', views.contact, name='contact'),
	path('movie/', views.view_movies, name='movies_listings'),
	path('movie/<movie_dir>/', views.movie, name='movie'),
	path('anime/', views.view_tv, name='tv_listings'),
	path('ongoing/', views.view_ongoing, name='ongoing_listings'),
	path('general-discussion/', views.general_discussion, name='discussion'),
	path('anime/<char>/', views.view_tv_char, name='tv_char'),
	path('movie/<char>/', views.view_movies_char, name='movies_char'),
	path('<anime_dir>/', views.detail, name='detail'),
	path('<anime_dir>/episode-<episode_number>/', views.episode, name='episode'),
]