from django.urls import path
from . import views
app_name = 'plants'
urlpatterns = [
    path('all/', views.all_plants, name='all_plants'),
    path('add/', views.add_plant, name='add_plant'),
    path('<int:plant_id>/', views.plant_detail, name='plant_detail'),
    path('update/<int:plant_id>/', views.update_plant, name='update_plant'),
    path('delete/<int:plant_id>/', views.delete_plant, name='delete_plant'),
    path('search/', views.search_plants, name='search_plants'),
]
