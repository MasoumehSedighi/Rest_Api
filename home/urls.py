from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'home'
urlpatterns = [
    path('one/', views.one, name='one'),
    # path('persons/', views.persons),
    # path('person/<str:name>/', views.person),
    # path('person_create/', views.person_create),
    # path('api-token-auth/', obtain_auth_token)
]

