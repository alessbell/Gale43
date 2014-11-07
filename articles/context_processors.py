from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404
from articles.models import Article

def articles_processor(request):
  articles = Article.objects.all()
  return {'articles': articles}