from rest_framework import serializers
from .models import Students

class studentSerializers(serializers.ModelSerializer):
    extra_data = serializers.JSONField(required=False, default=dict)

    class Meta:
        model = Students
        fields = '__all__'
        
    def create(self, validated_data):
        extra_fields = validated_data.pop('extra_data', {})
        student = Students.objects.create(**validated_data)
        student.save()
        return student