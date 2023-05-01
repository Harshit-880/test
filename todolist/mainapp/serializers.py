from rest_framework import serializers
from .models import *

class ToDOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields=('id','Title','Description','Date')