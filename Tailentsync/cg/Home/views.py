from django.shortcuts import render , HttpResponse , redirect
from django.utils import timezone
from django.contrib.auth import login as log, authenticate
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import logout
from Contact.models import Contact




def index(request):
    
 
    

     

 
    return render(request , 'Home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        #pass2 = request.POST.get('pass2')

        user = User.objects.create(username=username , email=email )
        user.set_password(password)
        user.save()

        return redirect('/login')
     

    return render(request, 'signup.html')


def signin(request):
     if request.method == 'POST':
         username = request.POST.get('uname')
         password = request.POST.get('pass1')

         if not User.objects.filter(username=username).exists():
             messages.error(request,"error user")
             return redirect('/signin')
         
         user = authenticate(username=username , password=password)
         if user is None:
             messages.error(request , 'error suer')
             return redirect('/signin')
         
         else:
             log(request , user)
             return redirect('/')

     return render(request , 'login.html')


# this is login reder code 
# def login(request):
#      if request.method == 'POST':
#          username = request.POST.get('uname')
#          password = request.POST.get('pass1')

#          if not User.objects.filter(username=username).exists():
#              messages.error(request,"error user")
#              return redirect('/signin')
         
#          user = authenticate(username=username , password=password)
#          if user is None:
#              messages.error(request , 'error suer')
#              return redirect('/signin')
         
#          else:
#              log(request , user)
#              return redirect('/')

#      return render(request , 'Home.html')





# def contacts(request):
#     if request.method == 'POST':
#         fname = request.POST.get('name')
#         email = request.POST.get('email')
#         number = request.POST('number')
#         description = request.POST('description')
#         feedback=Contact.objects.create(fname = fname,email=email, number=number , description=description)
#         feedback.save()
#     return render(request , "contacnnjnjnmnmnmt.html")



def logout_view(request):
    logout(request)
    return redirect('/login')

def login(request):
    return render(request , "Home.html")

def About(request):
    return render(request , "About.html")

def Assesment(request):
    return render(request , "Assesment.html")

def Blog(request):
    return render(request , "Blog.html")

# def Contact(request):
#     return render(request , "Contact.html")

def Footer(request):
    return render(request , "Footer.html")

def Courses(request):
    return render(request , "Courses.html")

def Dashboard(request):
    return render(request , "Dashboard.html")

def Faq(request):
    return render(request , "Faq.html")

def Library(request):
    return render(request , "Library.html")

def Navbar(request):
    return render(request , "Navbar.html")

def Quizlanding(request):
    return render(request , "Quizlanding.html")

def Quiz10(request):
    return render(request , "Quiz10.html")

def Innerlibrary(request):
    return render(request , "Innerlibrary.html")

def DashAbout(request):
    return render(request , "DashAbout.html")


def DashCourses(request):
    return render(request , "DashCourses.html")

def Dashteacher(request):
    return render(request , "Dashteacher.html")

def DashContact(request):
    return render(request , "DashContact.html")

def Dashplaylist(request):
    return render(request , "Dashplaylist.html")

def Dashviewprofile(request):
    return render(request , "Dashviewprofile.html")

def Servicesinnerlibrary(request):
    return render(request , "Servicesinnerlibrary.html")

def Diffenceinnerlibrary(request):
    return render(request , "Diffenceinnerlibrary.html")

def Designinnerlibrary(request):
    return render(request , "Designinnerlibrary.html")

def Engineeringinnerlibrary(request):
    return render(request , "Engineeringinnerlibrary.html")

def Lawinnerlibrary(request):
    return render(request , "Lawinnerlibrary.html")

def Marketinginnerlibrary(request):
    return render(request , "Marketinginnerlibrary.html")

def BoxFirst(request):
    return render(request , "BoxFirst.html")

def Box8th(request):
    return render(request , "Box8th.html")

def Box9th(request):
    return render(request , "Box9th.html")

def Box10th(request):
    return render(request , "Box10th.html")

def Box11th(request):
    return render(request , "Box11th.html")

def Teacherprofile(request):
    return render(request , "Teacherprofile.html")

def DashteacherRegister(request):
    return render(request , "DashteacherRegister.html")


def con(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        description = request.POST.get('description')
        feedback=Contact.objects.create(name = fname,email=email, number=number , description=description)
        feedback.save()
    return render(request , 'Contact.html')