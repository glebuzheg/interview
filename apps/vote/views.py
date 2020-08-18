from rest_framework import generics

from .models import VoteQuestion, VoteAnswer
from .serializers import VoteQuestionSerializer, VoteAnswerSerializer, VoteAnswerListSerializer, \
    UserAnswerListSerializer


class VoteQuestionListView(generics.ListAPIView):
    serializer_class = VoteQuestionSerializer

    def get_queryset(self):
        return VoteQuestion.objects.active()


class VoteAnswerAddView(generics.CreateAPIView):
    serializer_class = VoteAnswerSerializer


class VoteAnswersListView(generics.ListAPIView):
    serializer_class = VoteAnswerListSerializer

    def get_queryset(self):
        return VoteAnswer.objects.filter(question=self.kwargs.get('question_id'))


class UserAnswerListView(generics.ListAPIView):
    serializer_class = UserAnswerListSerializer

    def get_queryset(self):
        return VoteAnswer.objects.filter(user=self.kwargs.get('user_id'))
