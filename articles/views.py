from django.shortcuts import render, get_object_or_404
from .models import Article

def view_article(request, article_id):
    requested_article = get_object_or_404(Article, id=article_id)

    context = {
        "article": requested_article,
        "message": "Kevin is cool!",
    }

    return render(request, 'articles/view_article.html', context)

def all_articles(request):
    all_articles = Article.objects.all()

    context = {
        "articles": all_articles,
    }

    return render(request, 'articles/all_articles.html', context)