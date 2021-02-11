from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
	"""Создает пост с пользователем из settings"""
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_ate = timezone.now()
		self.save()

	def get_absolute_url(self):
		return reverse('post_list', kwargs={'slug': self.slug})

	def __str__(self):
		return self.title