from django.db import models

import markdown

from authentication.models import User


class Question(models.Model):
    """
    Quetion.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ('-update_date',)

    def __str__(self):
        return self.title

    def get_answers(self):    # 此方法可以获取问题相关的所有答案
        return Answer.objects.filter(question=self)

    def get_answers_count(self):    # 此方法获取问题的答案总数
        return Answer.objects.filter(question=self).count()

    def get_description_as_markdown(self): # 此方法将问题文本渲染为 Markdown 格式
        return markdown.markdown(self.description, safe_mode='escape')

class Answer(models.Model):
    """
    Answer for a question.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ('create_date',)

    def __str__(self):
        return self.description

    def get_description_as_markdown(self): # 此方法将回答文本渲染为 Markdown 格
        return markdown.markdown(self.description, safe_mode='escape')
