from django.shortcuts import render

from django.views.generic import DetailView, ListView

from .models import Post


class PostList(ListView):
	"""
	Получает список постов и выводит данные
	из базы, на гланный страницу
	"""
	model = Post
	posts = Post.objects.all()
	template_name = 'blog/post_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts'] = self.posts

		return context


class ViewPost(DetailView):
	"""Напровляет пользователя на опрделенную тему"""

	model = Post
	template_name = 'blog/post_detail.html'

