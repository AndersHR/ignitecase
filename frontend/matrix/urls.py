from django.urls import path

from . import views

urlpatterns = [
    path("", views.matrix_scatter_plot, name="matrix_scatter_plot"),
]