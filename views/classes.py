#_author:John
#date:2018/7/10 21:40
#softwave: PyCharm
from django.shortcuts import render,redirect
from stutens_manage import models
def get_classes(request):
    class_list = models.Classes.objects.all()
    return render(request, 'students_manage/get_classes.html', {'class_list':class_list})

def add_classes(request):
    if request.method == 'GET':
        return render(request, 'students_manage/add_classes.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        if title == '':
            return render(request, 'students_manage/add_classes.html')
        models.Classes.objects.create(title=title)
        return redirect('/stutens_manage/classes.html')

def del_classes(request):
    nid = request.GET.get('nid','')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/stutens_manage/classes.html')

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