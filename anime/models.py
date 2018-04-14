from django.db import models
from django.urls import reverse


class Genre(models.Model):
	genre_name = models.CharField(max_length=20)
	genre_order = models.PositiveIntegerField(default=1)

	class Meta:
		ordering = ['genre_order']

	def __str__(self):
		return self.genre_name	

class Anime(models.Model):
	anime_title = models.CharField(max_length=50)
	anime_slug = models.SlugField()
	anime_type = models.CharField(max_length=10)
	anime_status = models.CharField(max_length=10)
	anime_episodes = models.CharField(max_length=5, default='?')
	anime_cover = models.ImageField(upload_to='images/')
	genres = models.ManyToManyField(Genre)

	def __str__(self):
		return self.anime_title

	def get_absolute_url(self):
		return reverse('anime:detail', kwargs={'anime_dir': self.anime_slug})	


class Episode(models.Model):
	anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
	episode_title = models.CharField(max_length=20)
	episode_number = models.PositiveIntegerField(default = 0)
		
	def __str__(self):
		return self.episode_title

	def get_absolute_url(self):
		return reverse('anime:episode', kwargs={
			'anime_dir': self.anime.anime_slug, 
			'episode_number': self.episode_number
		})

