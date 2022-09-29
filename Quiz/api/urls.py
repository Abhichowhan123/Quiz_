from django.urls import path
from api import views

urlpatterns = [
    path('', views.home,name = "home"),
    path('<id>', views.quiz,name = "quiz"),
    path('api/<id>', views.api_question,name = "api_question"),
]
