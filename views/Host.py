#_author:John
#date:2018/7/18 0:49
#softwave: PyCharm
from django.shortcuts import redirect,render,HttpResponse
from django.contrib.auth.decorators import login_required
from stutens_manage.views import Login

@login_required()
def host_web(request):
    return render(request, 'students_manage/Host.html')