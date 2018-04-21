from django.contrib import admin

from .models import Anime, Episode, Genre, Studio, Premiere, Air_day, Movie, Message, Episodeurl, Movieurl

# admin.site.register(Anime)
admin.site.register(Episode)
admin.site.register(Genre)
admin.site.register(Studio)
admin.site.register(Premiere)
admin.site.register(Air_day)
admin.site.register(Message)
admin.site.register(Episodeurl)
admin.site.register(Movieurl)

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
	
	def get_genres(self, anime):
		genres = anime.genres.all()
		return ','.join([g.genre_name for g in genres])

	def get_studios(self, anime):
		studios = anime.studio.all()
		return	','.join([s.anime_studio for s in studios])

	get_studios.short_description = 'Studios'	
	get_genres.short_description = 'Genres'	

	list_display = ['anime_title', 'anime_type', 'anime_status', 'get_genres', 'get_studios', 'premiere']
	list_filter = ['anime_status', 'anime_type', 'genres', 'studio', 'premiere']
	prepopulated_fields = {'anime_slug': ('anime_title',)}
	filter_horizontal = ['genres', 'studio']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	
	def get_genres(self, movie):
		genres = movie.genres.all()
		return ','.join([g.genre_name for g in genres])

	def get_studios(self, movie):
		studios = movie.studio.all()
		return	','.join([s.anime_studio for s in studios])

	get_studios.short_description = 'Studios'	
	get_genres.short_description = 'Genres'	

	list_display = ['movie_title', 'movie_type', 'get_genres', 'get_studios', 'premiere']
	list_filter = ['movie_type', 'genres', 'studio', 'premiere']
	prepopulated_fields = {'movie_slug': ('movie_title',)}
	filter_horizontal = ['genres', 'studio']

