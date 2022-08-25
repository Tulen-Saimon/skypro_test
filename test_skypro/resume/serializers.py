from rest_framework import serializers

from .models import Resume


class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resume
        fields = (
            'status',
            'grade',
            'specialty',
            'salary',
            'education',
            'experience',
            'portfolio',
            'title',
            'phone',
            'email'
        )
