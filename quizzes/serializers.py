from rest_framework import serializers

from .models import *


class ListGroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('id', 'group_name')


class ListTestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Test
        fields = '__all__'


class RetrieveQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('question', 'photo_question')
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['answers'] = AnswerSerializer(instance.answers.all(), many=True).data
        return rep


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer', )


class AcceptAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Points
        fields = ('ans_id', 'timer')
    
    
