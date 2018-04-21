from django import forms

from .models import Anime, Message

class AnimeForm(forms.ModelForm):

	class Meta:
		model = Anime
		fields = [
			'anime_title',
			'anime_type',
			'anime_status',
			'anime_episodes',
			'genres',
			'premiere',
			'studio'
		]

class MessageForm(forms.ModelForm):
	
	class Meta:
		model = Message
		fields = [
			'name',
			'email',
			'subject',
			'message'
		]
		widgets = {
			'message': forms.Textarea
		}		