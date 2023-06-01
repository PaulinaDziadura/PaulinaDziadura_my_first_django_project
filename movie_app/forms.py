from django import forms

from my_first_django_project.movie_app.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"