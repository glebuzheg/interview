from django.urls import path

from .views import VoteListView

urlpatterns = [
    path('votes/', VoteListView.as_view()),
]
