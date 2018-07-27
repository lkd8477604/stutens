#_author:John
#date:2018/7/10 21:40
#softwave: PyCharm
from django.shortcuts import render,redirect
from stutens_manage import models
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from stutens_manage.views.Login import acc_login
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger

@login_required()
def get_classes(request):
    class_list = models.Classes.objects.all()
    p = Paginator(class_list, 2)
    page = request.GET.get('page', 1)
    try:
        class_list = p.page(int(page))
    except PageNotAnInteger:
        class_list = p.page(1)
    return render(request, 'students_manage/get_classes.html', {'class_list':class_list})

@login_required()
def add_classes(request):
    if request.method == 'GET':
        return render(request, 'students_manage/add_classes.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        if title == '':
            return render(request, 'students_manage/add_classes.html')
        models.Classes.objects.create(title=title)
        return redirect('/stutens_manage/classes.html')

@login_required()
def del_classes(request):
    nid = request.GET.get('nid','')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/stutens_manage/classes.html')

@login_required()
def edit_classes(request):
    if request.method == 'GET':
        nid = request.GET.get('nid', '')
        obj = models.Classes.objects.get(id=nid)
        return render(request,'students_manage/edit_classes.html', {'obj':obj})
    elif request.method == 'POST':
        nid = request.POST.get('nid', '')
        title = request.POST.get('xxoo', '')
        models.Classes.objects.filter(id=nid).update(title=title)
        return redirect('/stutens_manage/classes.html')

@login_required()
def set_teachers(request):
    nid = request.GET.get('nid', '')
    if request.method == 'GET':
        class_obj = models.Classes.objects.get(id=nid)
        cl_te_list = class_obj.teachers.all()
        al_te_list = models.Teachers.objects.all()
        return render(request, 'students_manage/set_teachers.html', {'class_obj':class_obj,
                                                                     'cl_te_list': cl_te_list,
                                                                     'al_te_list':al_te_list})
    elif request.method == 'POST':
        teachersID = request.POST.getlist('teachersID', '')
        id_int = []
        for i in teachersID:
            i = int(i)
            id_int.append(i)
        obj = models.Classes.objects.get(id = nid)
        obj.teachers.set(id_int)
        return redirect('/stutens_manage/classes.html')
