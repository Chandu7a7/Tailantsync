from django.shortcuts import render
from Courses.models import Course

# Create your views here.


def search_Courses(request):
    course = Course.objects.all()
    # # # products_to_display = products[:6]
    

    context={'course':course}   
    # print(course)



    return render(request , 'Courses.html', context )

def Courses(request):
    crs = Course.objects.all()
    context={
        'crs':crs
    }
    print(context)
    return render(request , 'Courses.html' , context)