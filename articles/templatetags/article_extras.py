from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django import template
from articles.models import Article

register = template.Library()

def show_articles(request):
  latest_article_list = Article.objects.order_by('-pub_date')[:5]
  context = {'latest_article_list': latest_article_list}
  return render(request, 'articles/_read_next.html', context)

register.simple_tag(show_articles)
