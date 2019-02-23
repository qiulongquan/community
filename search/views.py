from django.shortcuts import render, redirect
from django.db.models import Q

from questions.models import Question


def search(request):
    if 'q' not in request.GET:
        return redirect('')
    # 将关键词根据空格分开成为列表
    querystring = request.GET.get('q').strip()
    # 若没有输入信息
    if len(querystring) == 0:
        return redirect('home')
    # 在数据库中查找相关信息
    results = {'questions': Question.objects.filter(
        Q(title__icontains=querystring) |
        Q(description__icontains=querystring))}

    count = {'questions': results['questions'].count()}
    # 上下文
    context = {
        'hide_search': True,
        'querystring': querystring,
        'count': count['questions'],
        'results': results['questions']
    }

    return render(request, 'search/results.html', context)
