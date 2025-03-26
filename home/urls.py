from django.urls import path
from.import views

#List of URLS.
urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('gallery/',views.gallery),
    path('contact/',views.contact),
]