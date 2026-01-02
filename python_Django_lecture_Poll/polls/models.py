from django.db import models


class Question(models.Model):  # 모델 클래스를 상속해야 함!
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):  # 연산을 위해서 보통 사용
        return self.question_text

    #  def __repr__(self):  객체 찍기(표현) 하기 위해 보통 사용
    # id컬럼은 default로 지정
    # id -> primary key, Not Null, Unique
    # autoIncrement 특성을 가지는 정수형으로 지정됨
    # 자동지정해주므로 class에 써주진 않는다!


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # foreignkey는 _id가 붙음
    choice_text = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
# Create your models here.
