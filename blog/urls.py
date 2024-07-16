from . import views
from django.urls import path


urlpatterns = [path("", views.PoatList.as_view(), name="home")]