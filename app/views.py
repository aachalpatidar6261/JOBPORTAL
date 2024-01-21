from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def company_about(request):
    return render(request,'company_about.html')

def category(request):
    return render(request,'category.html')

def apply(request):
    try:
        company=User.objects.get(email=request.session['email'])
        if request.method=="POST":
            Apply.objects.create(            
                fullname=request.POST['fullname'],
                email=request.POST['email'],
                number=request.POST['number'],
                file=request.FILES['file'],        

            )
            msg="Job Add Successfully"
            return render(request,'apply.html',{'msg':msg})
        else:
            return render(request,'apply.html')
    except:
        return render(request,'login.html')

def job_list(request):
    jobs=Add_job.objects.all()
    return render(request,'job_list.html',{'jobs':jobs})

def company_index(request):
    return render(request,'company_index.html')




def company_add_jobs(request):
    company=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        Add_job.objects.create(
            company=company,
            keyword=request.POST['keyword'],
            category=request.POST['category'],
            location=request.POST['location']            
        )
        msg="Job Add Successfully"
        return render(request,'company_add_jobs.html',{'msg':msg})
    else:
        return render(request,'company_add_jobs.html')



def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        msg="Message Send Successfully"
        return render(request,'contact.html',{'msg':msg})
    else:
        return render(request,'contact.html')



def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.pwd==request.POST['pwd']:
                if user.user_type=="seeker":
                    request.session['email']=user.email
                    return redirect('index')
                else:
                    request.session['email']=user.email
                    return redirect('company_index')
            else:
                msg="Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        except:
            msg="Email Not Register"
            return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'login.html')
    
def logout(request):
    try:
        del request.session['email']       
        return redirect('logout')
    except:
        return render(request,'login.html')


def register(request):
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg="Email Already Exists"
            return render(request,'register.html',{'msg':msg})
        except:
            if request.POST['pwd']==request.POST['cpwd']:
                User.objects.create(
                    user_type=request.POST['user_type'],
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],                   
                    pwd=request.POST['pwd']                                        
                )
                msg="Email Register Successfully"
                return render(request,'login.html',{'msg':msg})
            else:
                msg="Password & Confirm Password Not Match"
                return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'register.html')
