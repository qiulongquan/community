from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,ListView,
)

from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


@method_decorator([login_required], name='dispatch')
class CreateQuestionView(CreateView):
    """
    Create a qeustion.
    """
    model = Question
    form_class = QuestionForm
    template_name = 'questions/ask_question.html'

    def form_valid(self, form):
        question = form.save(commit=False)
        question.user = self.request.user   # 设定问题提出人
        question.update_date = question.create_date
        question.save()
        form.save_m2m()
        messages.success(self.request, 'The question was created with success!')
        return redirect('questions:question_detail', question.pk)

class QuestionListView(ListView):
    """
    Show the list of questions.
    """
    model = Question
    ordering = ('update_date')
    context_object_name = 'questions'
    template_name = 'questions/questions_list.html'
    queryset = Question.objects.all()
    paginate_by = 1


class QuestionDetailView(CreateView):
    """
    Show question deatil.
    """
    model = Answer
    form_class = AnswerForm
    template_name = 'questions/question_detail.html'

    def get_context_data(self, **kwargs):
        question_id = self.kwargs.get('pk')
        question = Question.objects.get(pk=question_id)
        kwargs['question'] = question
        if Answer.objects.filter(question=question):
            kwargs['answers'] = Answer.objects.filter(question=question)

        context = super().get_context_data(**kwargs)
        return context

@login_required
def create_answer(request, pk):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = Answer()
            answer.user = request.user  # 设定回答提出人
            answer.question = Question.objects.get(pk=pk)
            answer.description = form.cleaned_data.get('description')
            answer.save()
            messages.success(request, 'The answer was created with success!')
            return redirect('questions:question_detail', answer.question.pk)
    else:
        form = AnswerForm()

    return redirect('questions:question_detail', pk)
