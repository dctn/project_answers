from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="home"),
    path("answer/<question_id>",views.answer,name="answer"),
    path("create/",views.create,name="create"),
    path("about",views.about,name="about"),
    path("delete_question/<question_id>",views.delete_question,name="delete_question"),
]
