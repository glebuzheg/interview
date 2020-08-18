from django.urls import path, include

urlpatterns = [
    path('votes/', include('apps.vote.urls')),
]
