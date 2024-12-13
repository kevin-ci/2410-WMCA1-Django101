from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Article
from .forms import ArticleForm
from functools import wraps


def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, "You do not have permission to access that page.")
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def view_article(request, article_id):
    requested_article = get_object_or_404(Article, id=article_id)

    context = {
        "article": requested_article,
    }

    return render(request, 'articles/view_article.html', context)

def all_articles(request):
    all_articles = Article.objects.all()

    context = {
        "articles": all_articles,
    }

    return render(request, 'articles/all_articles.html', context)

@superuser_required
def create_article(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, "Article created successfully!")
            return redirect('home')

    else: 
        # for the GET request (i.e. user types url into browser or clicks a link)
        article_form = ArticleForm()
        context  = {
            "form": article_form,
        }
        return render(request, 'articles/create_article.html', context)

@superuser_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, "Article updated successfully!")
            return redirect('home')

    else: 
        # for the GET request (i.e. user types url into browser or clicks a link)
        article_form = ArticleForm(instance=article)
        context  = {
            "form": article_form,
        }
        return render(request, 'articles/edit_article.html', context)

@superuser_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        article.delete()
        messages.success(request, "Article deleted successfully!")
        return redirect('home')
    else:
        return render(request, 'articles/delete_article.html')