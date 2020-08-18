from django.urls import path

from .views import VoteQuestionListView, VoteAnswersListView, VoteAnswerAddView, UserAnswerListView

urlpatterns = [
    path('questions/', VoteQuestionListView.as_view()),
    path('answer-add/', VoteAnswerAddView.as_view()),
    path('<int:question_id>/', VoteAnswersListView.as_view()),
    path('user/<int:user_id>/', UserAnswerListView.as_view()),

]
