from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('list/<int:page>', views.MovieList.as_view()),
    path('list/', RedirectView.as_view(url='1', permanent=True)),
]
