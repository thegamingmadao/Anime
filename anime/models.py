from django.db import models 
from django.urls import reverse

import random

class Air_day(models.Model):
	name = models.CharField(max_length=10, default='Monday')
	order = models.PositiveIntegerField(default=1)

	class Meta:
		ordering = ['order']

	def __str__(self):
		return self.name

class Genre(models.Model):
	genre_name = models.CharField(max_length=20)
	genre_order = models.PositiveIntegerField(default=1)

	class Meta:
		ordering = ['genre_order']

	def __str__(self):
		return self.genre_name

class Premiere(models.Model):
	premiere_year = models.CharField(max_length=20)

	def __str__(self):
		return self.premiere_year

class Studio(models.Model):
	anime_studio = models.CharField(max_length=20)

	def __str__(self):
		return self.anime_studio					

class Anime(models.Model):
	anime_title = models.CharField(max_length=50)
	anime_slug = models.SlugField()
	anime_type = models.CharField(max_length=10)
	anime_status = models.CharField(max_length=10)
	anime_episodes = models.CharField(max_length=5, default='?')
	anime_cover = models.ImageField(upload_to='images/')
	anime_publication_date = models.DateTimeField(blank=True, null=True)
	anime_count = models.PositiveIntegerField(default=0)
	genres = models.ManyToManyField(Genre)
	premiere = models.ForeignKey(Premiere, on_delete=models.CASCADE)
	studio = models.ManyToManyField(Studio)
	day = models.CharField(max_length=10, default='Monday')

	def __str__(self):
		return self.anime_title

	def get_absolute_url(self):
		return reverse('anime:detail', kwargs={'anime_dir': self.anime_slug})

	def get_genres(self):
		genres = self.genres.all()
		return ','.join([g.genre_name for g in genres])

	def get_studios(self):
		studios = self.studio.all()
		return	','.join([s.anime_studio for s in studios])

	def get_random_anime():
		max_id = Anime.objects.latest('pk').pk
		pk = random.randint(1, max_id)
		return Anime.objects.get(pk=pk)

	def get_latest_animes():
		return	Anime.objects.order_by('-anime_publication_date')[:10]

	def most_views():
		return Anime.objects.order_by('-anime_count')[:10]

	def trending_anime():
		return Anime.objects.filter(anime_status='Ongoing').order_by('-anime_count')[:10]		

class Movie(models.Model):
	movie_title = models.CharField(max_length=50)
	movie_slug = models.SlugField()
	movie_type = models.CharField(max_length=10)
	movie_cover = models.ImageField(upload_to='images/')
	movie_publication_date = models.DateTimeField(blank=True, null=True)
	movie_count = models.PositiveIntegerField(default=0)
	genres = models.ManyToManyField(Genre)
	premiere = models.ForeignKey(Premiere, on_delete=models.CASCADE)
	studio = models.ManyToManyField(Studio)

	def __str__(self):
		return self.movie_title

	def get_absolute_url(self):
		return reverse('anime:movie', kwargs={'movie_dir': self.movie_slug})

	def get_genres(self):
		genres = self.genres.all()
		return ','.join([g.genre_name for g in genres])

	def get_studios(self):
		studios = self.studio.all()
		return	','.join([s.anime_studio for s in studios])

	def get_random_movie():
		max_id = Movie.objects.latest('pk').pk
		pk = random.randint(1, max_id)
		return Movie.objects.get(pk=pk)

	def get_latest_movies():
		return	Movie.objects.order_by('-movie_publication_date')[:10]

	def most_views():
		return Movie.objects.order_by('-movie_count')[:10]		
							

class Episode(models.Model):
	anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
	episode_publication_date = models.DateTimeField(blank=True, null=True)
	episode_title = models.CharField(max_length=20)
	episode_number = models.PositiveIntegerField(default = 0)
	episode_count = models.PositiveIntegerField(default = 0)
		
	def __str__(self):
		return self.episode_title

	def get_absolute_url(self):
		return reverse('anime:episode', kwargs={
			'anime_dir': self.anime.anime_slug, 
			'episode_number': self.episode_number
		})

	def get_latest_episodes():
		return	Episode.objects.order_by('-episode_publication_date')[:100]

class Message(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	subject = models.CharField(max_length=250)
	message = models.CharField(max_length=1000)
	date = models.DateTimeField(auto_now_add=True)

class Episodeurl(models.Model):
	video = models.ForeignKey(Episode, on_delete=models.CASCADE)
	host = models.CharField(max_length=20)
	video_url = models.CharField(max_length=250)
	video_quality = models.PositiveIntegerField(default = 0)

class Movieurl(models.Model):
	video = models.ForeignKey(Movie, on_delete=models.CASCADE)
	host = models.CharField(max_length=20)
	video_url = models.CharField(max_length=250)
	video_quality = models.PositiveIntegerField(default = 0)	

	


