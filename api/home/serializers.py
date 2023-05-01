from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        # fields = ['name', 'age']
       
        fields = '__all__'


    def validate(self, data):
        if data['age']<18:
            raise serializers.ValidationError({'error': "age cannot be less than 18"})
        
        return data