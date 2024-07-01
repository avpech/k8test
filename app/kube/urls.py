from django.urls import path

from kube import views

urlpatterns = [
    path("", views.hello_from_kuber, name="hello"),
]
