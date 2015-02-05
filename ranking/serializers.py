from ranking.models import Course, Teacher, Subject
from rest_framework import serializers

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'degree', 'score')