from .models import Myuser
from rest_framework import serializers


class MyuserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Myuser
        fields=['id','first_name','last_name','email','created_at','updated_at']
        
        read_only_fields=('id','created_at','updated_at')