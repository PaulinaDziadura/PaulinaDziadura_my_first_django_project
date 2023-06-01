from django.shortcuts import render, redirect

from django.http import HttpResponse
import random

from django.views import View
from models import Article
from models import Comment
import os
from django.conf import settings


class ArticleAdd(View):
    def get(self, request):
        message = "Dodaj artykuł"
        return render(request, "blog_add.html", {"message": message})

    def post(self, request):
        title = request.POST.get("title")
        author = request.POST.get("author")
        description = request.POST.get("description")

        article = Article.objects.create(title=title,
                                         author=author, description=description)
        return redirect("/blog/")


def article_list(request):
    articles = Article.objects.all()
    return render(request, "article_list.html", {"articles": articles})


class ArticleEdit(View):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        message = "Zapisz zmiany"
        return render(request, "blog_add.html", {"article": article, "message": message})

    def post(self, request, pk):
        article = Article.objects.get(pk=pk)
        title = request.POST.get("title")
        author = request.POST.get("author")
        description = request.POST.get("description")
        article.title = title
        article.author = author
        article.description = description
        article.save()
        return redirect("/blog/")


class ArticleDelete(View):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        return render(request, "article_delete.html",
                      {"article": article})

    def post(self, request, pk):
        delete = request.POST.get("delete")
        if delete is not None:
            article = Article.objects.get(pk=pk)
            article.delete()
        return redirect("/blog/")


class CommentAdd(View):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        message = "Dodaj komentarz"
        return render(request, "blog_show.html", {"article": article, "message": message})

    def post(self, request, pk):
        article = Article.objects.get(pk=pk)
        com_author = request.POST.get("com_author")
        com_message = request.POST.get("com_message")
        Comment.objects.create(author=com_author, message=com_message, article=article)
        return render(request, "blog_show.html",
                      {"article": article})
