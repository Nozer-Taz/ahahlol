from django.urls import path

from .views import *


urlpatterns = [
    path('group-list/', ListGroupView.as_view()),
    path('test-list/', ListTestView.as_view()),
    path('question/<int:pk>/', RetrieveQuestionView.as_view()),
    path('answer/', count),
]
