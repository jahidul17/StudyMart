from rest_framework import serializers
from .models import Aiquest


class AiquestSerializer(serializers.ModelSerializer):
    class Meta:
        model =Aiquest
        fields=['id','teacher_name','course_name','course_duration','seat']

