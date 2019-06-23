from django.urls import path
from . import views

# start with article
urlpatterns = [
    # http://localhost:8000/article_list/
    path('', views.article_list, name='article_list'),
    #path('<int:article_pk>', views.article_detail, name="article_detail"),

]