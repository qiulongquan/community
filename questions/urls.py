from django.urls import include, path

from .views import (
    CreateQuestionView, QuestionDetailView,
    QuestionListView,
)
from .views import create_answer

app_name = 'questions'    # 指定了路由名称

urlpatterns = [
    path('questions/', include(([
        path('', QuestionListView.as_view(), name='question_list'),
        path('add/', CreateQuestionView.as_view(), name='question_add'),
        path('<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
        path('<int:pk>/add', create_answer, name='answer_add'),
    ])))
]