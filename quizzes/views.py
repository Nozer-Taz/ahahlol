from phonenumbers import is_valid_number
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import GenericViewSet

from quizzes.models import *
from quizzes.serializers import *


class ListGroupView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = ListGroupSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ListGroupSerializer(queryset, many=True)
        return Response(serializer.data)


class ListTestView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = ListTestSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ListTestSerializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveQuestionView(generics.RetrieveAPIView):
    
    queryset = Question.objects.all()
    serializer_class = RetrieveQuestionSerializer

@api_view(['POST'])
def count(request):
    serializer = AcceptAnswerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)





# class AcceptUserAnswer(generics.UpdateAPIView):

#     queryset = Points.objects.all()
#     serializer_class = AcceptAnswerSerializer







# @api_view(['POST'])
# def count_points(request, a_id):
#     user = request.user
#     answer_id = request.POST.get('ans_id')
#     time = request.POST.get('timer')

#     get_answer = Answer.objects.get(id=answer_id)

#     if get_answer.is_correct == True:
#         if time <= 1:
#             result = 100 - (100/(20*time)) +(100/20)
#             points = Points.objects.get(points=points)
#         else:
#             result = 100 - (100/(20*time))
        
