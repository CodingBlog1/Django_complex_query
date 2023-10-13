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
        print(validated_data)
        return City.objects.create(**validated_data)
    
    
class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    
    def create(self, validated_data):
        print(validated_data)
        visit_city001 = tuple(validated_data['visit_city'])
        print(visit_city001,'modifie')
        for i in validated_data["visit_city"]:
            if not City.objects.filter(id=i.id).exists():
                City.objects.create(name="this", provision=255)
        
        return super().create(validated_data)
        
    #     return Person.objects.create(**modified_data)    
    
    
    #     {
    #     "first_name":"morgun",
    #     "last_name":"daa",
    #     "visit_city":[6,7],
    #     "hometown":7,
    #     "living":6

    # }