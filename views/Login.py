#_author:John
#date:2018/7/17 22:06
#softwave: PyCharm
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    return redirect('/stutens_manage/classes.html')


def acc_login(request):
    if request.method == 'POST':
        print (request.POST.get('username'), request.POST.get('password'))
        user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
        print (user)
        if user is not None:
            login(request,user)
            return redirect('/stutens_manage/classes.html')
        else:
            login_err = 'Wrong password or username!!!'
            return render(request, 'students_manage/index.html', {'login_err': login_err})
    return render(request, 'students_manage/index.html')

def log_out(request):
    logout(request)
    return redirect('/stutens_manage/index.html')