"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('hello/',views.hello),
    path('add/',views.add),
    path('brothers/',views.brothers),
    path('fibonacci/',views.fibonacci),
    path('multiply/', views.multiply),
    path('game_guess/', views.game_guess),
    path ('article/<int:id>/', views.article),
    path ('greetings/<str:name>/<int:repeat>/', views.greetings),
    path('calc/<str:number_a>/<str:operation>/<str:number_b>/', views.calc),
    path('random_generator/<int:min>/<int:max>/', views.random_generator),
    path('random_generator/<int:min>/<int:max>/<int:throw>', views.random_generator),
    path('template/', views.show_template),
    path('FizzBuzz/', views.fizz_buzz),
    path('multiply/', views.multiply),
    path('form/', views.form),
    path('login/',views.login_user),
    path('add_product/',views.add_product),
    path ('product_show/', views.product_show),
    path ('test/', views.TestView.as_view()),
    path ('test/show', views.ShowTestView.as_view()),
    path ('pizza/', views.PizzaView.as_view()),
    path ('car/', views.CarView.as_view()),
    path ('login_class/', views.LogView.as_view()),
    path('game/', include('django_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('movie', include ('movie_app.urls'))
]
