from django.contrib import admin

from .models import Anime, Episode, Genre

# admin.site.register(Anime)
admin.site.register(Episode)
admin.site.register(Genre)

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
	
	def get_genres(self, anime):
		genres = anime.genres.all()
		return ','.join([g.genre_name for g in genres])

	get_genres.short_description = 'Peos'	

	list_display = ['anime_title', 'anime_type', 'anime_status', 'get_genres']
	list_filter = ['anime_status', 'anime_type', 'genres']
	prepopulated_fields = {'anime_slug': ('anime_title',)}
	filter_horizontal = ['genres']

