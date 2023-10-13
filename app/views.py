from django.shortcuts import render
from rest_framework import generics
from .serializer import CountrySerializers,CitySerializers,PersonSerializers
from rest_framework.response import Response
from .models import City,Person,Province
from django.db.models import Q
# Create your views here.

class ProvinceCountry(generics.GenericAPIView):
    serializer_class = CountrySerializers
    
    def post(self,request):
        data = request.data
        for c in data:
            serializer = self.serializer_class(data={"name":c})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = serializer.data
        return Response(data,status=200)


class CityApi(generics.GenericAPIView):
    serializer_class = CitySerializers
    
    def post(self,request):
        data = request.data
        serialier = self.serializer_class(data=data)
        serialier.is_valid(raise_exception=True)
        serialier.save()
        data = serialier.data
        return Response(data,status=200)
    
class PersonApi(generics.GenericAPIView):
    serializer_class = PersonSerializers
    
    def post(self,request):
        data = request.data
        serialier = self.serializer_class(data=data)
        serialier.is_valid(raise_exception=True)
        serialier.save()
        data = serialier.data
        return Response(data,status=200)
        

class TestComplexQueries(generics.GenericAPIView):
    def get(self,request):
        pass
        #select select_related query
        # country = City.objects.select_related('province')
        # Person.objects.select_related('living').filter(living__name='ghaziabad')
        # print(country.query,'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
        # for i in country:
        #     print(i.province,'0000000000000000000000000000000000000000000000000')
        
        # prefetch_related query
        # db = Province.objects.prefetch_related('city_set').get(name__iexact='Benin')
        # for i in db.city_set.all():
            # print(i.name)
            
        # Q complex query
        # data = Person.objects.select_related('living').filter(living__name='ghaziabad')
        # print(data)
        # for i in data:
        #     print(i.living)
        
        
        return Response()