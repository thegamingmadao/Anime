from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.db.models import Q

from .models import Anime, Episode, Air_day, Movie
from .forms import MessageForm

def index(request):
	episodes = Episode.get_latest_episodes()
	paginator = Paginator(episodes, 10)
	
	page = request.GET.get('page')
	episodes = paginator.get_page(page)
	
	latest = Anime.get_latest_animes()
	trending = Anime.trending_anime()
	random_anime = Anime.get_random_anime()
	random_movie = Movie.get_random_movie()
	return render(request, 'anime/index.html', {
		'random_anime': random_anime,
		'random_movie':	random_movie,
		'episodes': episodes,
		'latest': latest,
		'trending': trending
	})

def detail(request, anime_dir):
	anime = get_object_or_404(Anime, anime_slug=anime_dir)
	genres = anime.get_genres()
	studios = anime.get_studios()
	return render(request, 'anime/detail.html', {
		'anime': anime,
		'genres': genres,
		'studios': studios
	})

def episode(request, anime_dir, episode_number):
	anime = get_object_or_404(Anime, anime_slug=anime_dir)
	episodes = Episode.objects.filter(anime__anime_slug=anime_dir)
	paginator = Paginator(episodes, 1)
	
	page = request.GET.get('page')
	episodes = paginator.get_page(page)
	episode = get_object_or_404(
		Episode, episode_number=episode_number, anime__anime_slug=anime_dir
	)
	episode.episode_count += 1
	anime.anime_count += 1
	anime.save()
	episode.save()
	return render(
		request,'anime/episode.html', {
			'episode': episode, 'anime': anime, 'episodes': episodes
		}
	)

def movie(request, movie_dir):
	anime = get_object_or_404(Movie, movie_slug=movie_dir)
	anime.movie_count += 1
	anime.save()
	genres = anime.get_genres()
	studios = anime.get_studios()
	return render(request, 'anime/movie.html', {
		'anime': anime,
		'genres': genres,
		'studios': studios
	})

def search(request):
	query = request.GET.get('q')
	# query_filter = None
	# if query:
	# 	for word in query.split():
	# 		query_filter_aux = Q(anime_title__icontains=word)
	# 		query_filter = ( query_filter_aux & query_filter ) if bool( query_filter ) else query_filter_aux
	# 	results	= Anime.objects.filter(query_filter)
	# else:
	# 	results = Anime.objects.all()	
	results1 = Anime.objects.filter(anime_title__icontains=query)
	results2 = Movie.objects.filter(movie_title__icontains=query)
	results = list(results1)
	results.extend(list(results2))
	paginator = Paginator(results, 24)
	
	page = request.GET.get('page')
	results = paginator.get_page(page)
	return render(request, 'anime/search.html', {
		'q': query,
		'results': results
	})

def view_movies(request):
	anime = Movie.objects.all()
	paginator = Paginator(anime, 24)
	
	page = request.GET.get('page')
	anime = paginator.get_page(page) 
	return render(request, 'anime/movie-listings.html', {
		'anime': anime
	})	

def view_tv(request):
	anime = Anime.objects.all()
	paginator = Paginator(anime, 24)
	
	page = request.GET.get('page')
	anime = paginator.get_page(page)
	return render(request, 'anime/listings.html', {
		'anime': anime
	})

def view_ongoing(request):
	anime = Anime.objects.filter(anime_status='Ongoing')
	days = Air_day.objects.all()
	return render(request, 'anime/ongoing.html', {
		'anime': anime,
		'days': days
	})

def view_movies_char(request, char):
	anime = Movie.objects.filter(movie_title__startswith=char)
	paginator = Paginator(anime, 24)
	
	page = request.GET.get('page')
	anime = paginator.get_page(page)
	return render(request, 'anime/movie-listings.html', {'anime': anime})

def view_tv_char(request, char):
	anime = Anime.objects.filter(anime_title__startswith=char)
	paginator = Paginator(anime, 24)
	
	page = request.GET.get('page')
	anime = paginator.get_page(page)
	return render(request, 'anime/listings.html', {'anime': anime})

def general_discussion(request):
	return render(request, 'anime/general_discussion.html', {
		'message': 'Welcome to general discussion board!'
	})

def contact(request):
	form = MessageForm(request.POST or None)
	success = False
	if form.is_valid():
		message = form.save()
		success = True
		# message.name = request.POST.get('name')
		# message.email = request.POST.get('email')
		# message.subject = request.POST.get('subject')
		# message.message = request.POST.get('message')
		# message.save()
		form = MessageForm()
		#return render(request, 'anime/contact.html', {'form': form})	
	return render(request, 'anime/contact.html', {
		'form': form,
		'success': success
	})

def test(request):
	return render(request, 'anime/test.html')