from django.shortcuts import get_object_or_404, render
#from django.db.models import Q



from .models import Anime, Episode

def index(request):
	anime = Anime.objects.all()
	return render(request, 'anime/index.html', {'anime': anime})

def detail(request, anime_dir):
	anime = get_object_or_404(Anime, anime_slug=anime_dir)
	return render(request, 'anime/detail.html', {'anime': anime})

def episode(request, anime_dir, episode_number):
	anime = get_object_or_404(Anime, anime_slug=anime_dir)
	episode = get_object_or_404(
		Episode, episode_number=episode_number, anime__anime_slug=anime_dir
	)
	return render(
		request,'anime/episode.html', {
			'episode': episode, 'anime': anime
		}
	)

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
	results = Anime.objects.filter(anime_title__icontains=query)
	return render(request, 'anime/search.html', {'results': results})
			

