from articles.models import Article

def articles_processor(request):
  articles = Article.objects.all()
  return {'articles': articles}