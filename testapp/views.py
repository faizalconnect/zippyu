# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .models import Post


# Create your views here.
def hello_world(request):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	STATIC_ROOT = os.path.join(os.path.abspath(
    os.path.join(BASE_DIR,  'static')), '')
	list_arr = os.listdir('.')
	data = ' '.join(str(data) for data in list_arr)

	post = Post.objects.create(
	title = 'Hello MongoDB!',
	text = 'Just wanted to drop a note from Django. Cya!',
	tags = ['mongodb', 'django']
	)
	print post.comments
	post.comments.extend(['Great post!', 'Please, do more of these!'])
	post.save()
	print Post.objects.get().comments
	return HttpResponse(data)
