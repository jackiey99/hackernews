from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
	news_list = News.objects.all()
	paginator = Paginator(news_list, 10)

	page = request.GET.get('page')
	print page
	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		news = paginator.page(1)
	except EmptyPage:
		news = paginator.page(paginator.num_pages)


	context = {'news' : news}
	return render(request, 'hackernews/index.html', context)