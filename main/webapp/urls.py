from .views import IndexView

from django.urls import path

app_name = 'webapp'

urlpatterns = [
    path("", IndexView.as_view()),
]