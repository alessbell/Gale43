from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404

from articles.models import Article

# Create your views here.

def index(request):
  latest_article_list = Article.objects.order_by('-pub_date')[:5]
  context = {'latest_article_list': latest_article_list}
  return render(request, 'articles/index.html', context)

def detail(request, article_id):
  try:
    article = Article.objects.get(pk=article_id)
  except Article.DoesNotExist:
    raise Http404
  return render(request, 'articles/article.html', {'article':article})

def show_articles(request):
  latest_article_list = Article.objects.order_by('-pub_date')[:5]
  context = {'latest_article_list': latest_article_list}
  return render(request, 'articles/_read_next.html', context)