from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.getNotes, name="notes"),
    path('note/<str:pk>', views.getNote, name="note"),
]