#_author:John
#date:2018/7/10 21:40
#softwave: PyCharm
from django.shortcuts import render,redirect
from stutens_manage import models

def get_students(request):
    stu_list = models.Students.objects.all()
    return render(request, 'students_manage/get_students.html', {'stu_list':stu_list})

def del_students(request):
    nid = request.GET.get('nid', '')
    models.Students.objects.filter(id= nid).delete()
    return redirect('/stutens_manage/students.html')

def edit_students(request):
    if request.method == 'GET':
        nid = request.GET.get('nid', '')
        obj = models.Students.objects.get(id = nid)
        cs_list = models.Classes.objects.all()
        return render(request, 'students_manage/edit_students.html', {'obj':obj,'cs_list':cs_list})
    elif request.method == "POST":
        nid = request.POST.get('nid', '')
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        classes = request.POST.get('classes', '')
        gender = request.POST.get('gender', '')
        models.Students.objects.filter(id=nid).update(
            name=name,
            age=age,
            classes_id=classes,
            gender=gender,
        )
        return redirect('/stutens_manage/students.html')

def add_students(request):
    if request.method == 'GET':
        cs_list = models.Classes.objects.all()
        return render(request, 'students_manage/add_students.html', {'cs_list':cs_list})
    elif request.method == 'POST':
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        classes = request.POST.get('classes', '')
        gender = request.POST.get('gender', '')
        models.Students.objects.create(
            name=name,
            age=age,
            classes_id=classes,
            gender=gender,
        )
        return redirect('/stutens_manage/students.html')

