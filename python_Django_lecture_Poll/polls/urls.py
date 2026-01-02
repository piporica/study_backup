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
from django.urls import path   # include 인클루드는 계층용
from . import views

# /여기는 polls 안의 url!
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:q_id>/', views.detail, name='detail'),  # 꺽쇠 - 데이타추출
]

