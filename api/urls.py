from django.urls import path
from hackathons.views import hackathons, sign_up, login, register_in_hackathon, user_hackathon, create_submission

urlpatterns = [
    path('hackathons/', hackathons),
    path('hackathons/<str:id>/', create_submission),
    path('hackathons/<str:id>/register', register_in_hackathon),
    path('signup/', sign_up),
    path('login/', login),
    path('user/', user_hackathon)
]
