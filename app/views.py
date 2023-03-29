from django.shortcuts import render, get_object_or_404
from app.models import StudentInfo

# Create your views here.


def student_details(request, id_):
    foo = StudentInfo.objects.get(id=id_)
    ################################################
    #                                              #
    # get_obj_or_404                               #
    # foo = get_object_or_404(StudentInfo, pk=id_) #
    #                                              #
    ################################################
    return render(request, "app/info.html", {"details": foo})


def students_detail(request):
    foo = StudentInfo.objects.all()
    return render(request, "app/all_stu_info.html", {"details": foo})
