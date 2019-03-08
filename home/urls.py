from django.urls import path

from . import views

from .views import house_details, home_view, for_rent_view, for_sale_view, favourite_view

app_name = "home"

urlpatterns = [
    #path('', views.home_view, name="home"),
    path('', home_view.as_view(), name="home"),
    path('for-rent/', for_rent_view.as_view(), name="for_rent"),
    path('for-sale/', for_sale_view.as_view(), name="for_sale"),
    path('favourite/', favourite_view.as_view(), name="favourites"),
    path('house/<int:pk>/', house_details.as_view(), name="details"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]
