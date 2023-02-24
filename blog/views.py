from django.shortcuts import render
from blog.models import Article
from django.utils.translation import gettext as _


global_context = {
    'author_name': _('Александр Бейнар'),
}


def home_page(request):
    articles = Article.objects.all()
    context = global_context | {
        'articles': articles,
    }
    return render(request, 'home_page.html', context)


def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = global_context | {
        'article': article,
    }
    return render(request, 'article_page.html', context)


def category_page(request, category):
    articles = Article.objects.filter(category=category)
    context = global_context | {'articles': articles, 'category': category}
    return render(request, 'category_page.html', context)
