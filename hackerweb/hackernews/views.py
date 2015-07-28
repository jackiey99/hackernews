from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
# Create your views here.

def index(request):
	news_list = News.objects.all()
	paginator = Paginator(news_list, 10)

	page = request.GET.get('page')
	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)


	context = {'news' : news}
	return render(request, 'hackernews/index.html', context)

def gen_wordcloud(request):
	topic_text = ''
	news_list = News.objects.all()
	for news in news_list:
		topic_text += news.title

	wordcloud = WordCloud().generate(topic_text)
	# Open a plot of the generated image.
	imgplot = plt.imshow(wordcloud)
	plt.axis("off")
	plt.savefig('hackernews/static/wordcloud.png',bbox_inches='tight')
	context = {'image_path' :'True'}
	return render(request, 'hackernews/wordcloud.html', context)