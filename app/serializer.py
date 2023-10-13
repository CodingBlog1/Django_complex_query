from rest_framework import serializers 
from .models import Province,City,Person

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'
        
    def validate(self, attrs):
        
        name1 = attrs.get('name')        
        if name1 is None:
            raise serializers.ValidationError(self.default_error_messages)
        if Province.objects.filter(name=name1).exists():
            raise serializers.ValidationError("coutry name already exist try diffrent")
      
        return attrs
    
    def create(self, validated_data):
        return Province.objects.create(**validated_data)
    
    
    
   
   
class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model=City
        fields='__all__'
        
    def create(self, validated_data):
        return City.objects.create(**validated_data)
    
    
class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        return Person.objects.create(**validated_data)    
    