#_author:John
#date:2018/7/16 22:53
#softwave: PyCharm
from django.shortcuts import redirect,render,HttpResponse
from stutens_manage import models

def del_classes(request):
    nid = request.GET.get('nid', '')
    msg = '成功'
    try:
        models.Classes.objects.get(id=nid).delete()
    except Exception as e:
        msg = str(e)
    return HttpResponse(msg)