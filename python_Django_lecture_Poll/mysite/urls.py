"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # 인클루드는 계층용
from polls import views

# /admin 눌렀을 시...
# /polls -> 모든 투표 질문을 화면에 출력
# 2번째 인자 : 입력 URL을 처리할 함수를 명시 - View 안의 함수
# 이거 순서대로 찾음 - 순서 중요!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include ('polls.urls'))  # 논리적인 이름임
]

