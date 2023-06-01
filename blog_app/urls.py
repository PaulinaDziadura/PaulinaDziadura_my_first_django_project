from django.urls import path
from . import views
urlpatterns=[
    path('add/', views.ArticleAdd.as_view()),
    path('', views.article_list),
    path('edit/<int:pk>', views.ArticleEdit.as_view()),
    path('delete/<int:pk>', views.ArticleDelete.as_view()),
    path ('show/<int:pk>',views.CommentAdd.as_view())]