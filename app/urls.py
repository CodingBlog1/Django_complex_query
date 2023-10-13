from django.urls import path
from .views import ProvinceCountry,TestComplexQueries,CityApi
urlpatterns = [
    
    path('country/',ProvinceCountry.as_view()),
    path('test/',TestComplexQueries.as_view()),
    path('city/',CityApi.as_view()),
    
]