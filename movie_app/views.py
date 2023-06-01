from django.shortcuts import render
from django.views import View

from my_first_django_project.movie_app.forms import MovieForm



class MovieDjangoForm(View):
    def get(self,request,pk):
        form = MovieForm()
        return render (request, "movie_django_form.html", {"form":form})
    def post(selfself,request):
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("/movie")
        else:
            return render (request, "movie_django_form.html", {"form":form})