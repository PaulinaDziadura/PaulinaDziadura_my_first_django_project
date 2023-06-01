from django.urls import path
from . import views
urlpatterns=[
    path('add/', views.GameAdd.as_view()),
    path('', views.game_list),
    path('edit/<int:pk>', views.GameEdit.as_view()),
    path('delete/<int:pk>', views.GameDelete.as_view())]