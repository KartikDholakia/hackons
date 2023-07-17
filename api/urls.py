from django.urls import path
from hackathons.views import hackathons, sign_up, login

urlpatterns = [
    path('hackathons/', hackathons),
    path('signup/', sign_up),
    path('login/', login)
]
