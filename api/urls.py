from django.urls import path
from hackathons.views import hackathons

urlpatterns = [
    path('hackathons/', hackathons),
]
