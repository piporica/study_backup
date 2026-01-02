from django.shortcuts import render, get_object_or_404
from polls.models import *

# 클라이언트가 서버에 요청을 보내는 작업을 리퀘스트라고 함
# 클라이언트가 서버에 요청을 보낼 때 여러가지 정보가 같이 서버에 제공됨
# 서버 -> 클라이언트는 리스폰스


def index(request):
    # 로직 처리 코드가 나옴
    # Question class의 객체 3개를 생성 : 그 3개를 list 안에 넣어줘야댐
    tmp = Question.objects.all().order_by('-pub_date')[:3] # 슬라이싱하면 자를수있음~
    context = {'latest_question_list': tmp}
    return render(request, 'index.html', context)

# Create your views here.


def detail(request, q_id):
    # 이번에는 특정 퀘스천객체 하나만 필요!
    tmp = get_object_or_404(Question, pk=q_id)
    context = {'question': tmp}
    return render(request, 'detail.html', context)

