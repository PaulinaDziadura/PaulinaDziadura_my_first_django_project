from django.contrib import admin

# Register your models here.
from movie_app.models import Movie, Ticket, Payment
admin.site.register(Movie)
admin.site.register(Ticket)
admin.site.register(Payment)
