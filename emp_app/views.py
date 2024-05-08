from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def deps(dept):
    team_names = ["HR","Python Development","Data Science","App Development","Web Development","SDE Team","DevOps","ML Ops",]
    x=-1
    for i in team_names:
        x=x+1
        if i == dept:
            return x
def rols(reles):
    ro=['Manager','Head','Junior Developer','Senior Developer','Tester','DBMS Admin','Front End Dev','Back End Dev']
    x=-1
    for i in ro:
        x=x+1
        if i == reles:
            return x


def index(request):
    return render(request, 'index.html')
    
def employee(request):  # sourcery skip: extract-method
    if request.method=="POST":
        data=request.POST
        img=request.FILES.get('img')
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        add=data.get('add')

        depts=data.get('dept')
        depts=deps(depts)
        departments_objs=Department.objects.all()
        dept=departments_objs[depts]

        salary=data.get('salary')
        bonus=data.get('bonus')
        phone=data.get('phone')

        roles=data.get('role')
        roles=rols(roles)
        roles_objs=Role.objects.all()
        role=roles_objs[roles]

        hire_date=data.get('hire_date')

        Employee.objects.create(img=img,first_name=first_name,
                               last_name=last_name,dept=dept,
                               salary=salary,bonus=bonus,
                               phone=phone,role=role,
                               hire_date=hire_date,
                               add=add,
                               )
        return redirect('/view_emp/')
    
    queryset=Employee.objects.all()
    context={'employee':queryset}
    return render(request, 'employee.html',context)



def view_emp(request):
    queryset=Employee.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(first_name__icontains=request.GET.get('search'))

    context={'employee':queryset}
    return render(request, 'view_emp.html',context)

@login_required(login_url='/login/')
def delete_emp(request,id):
    queryset=Employee.objects.get(id=id)
    queryset.delete()
    return redirect("/view_emp/")

@login_required(login_url='/login/')
def update_emp(request,id):
    # sourcery skip: extract-duplicate-method, extract-method, inline-immediately-returned-variable
    queryset=Employee.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        img=request.FILES.get('img')
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        add=data.get('add')

        depts=data.get('dept')
        depts=deps(depts)
        departments_objs=Department.objects.all()
        dept=departments_objs[depts]

        salary=data.get('salary')
        bonus=data.get('bonus')
        phone=data.get('phone')

        roles=data.get('role')
        roles=rols(roles)
        roles_objs=Role.objects.all()
        role=roles_objs[roles]
        queryset.first_name = first_name  # Issue might be here
        queryset.last_name = last_name
        queryset.add = add
        queryset.dept = dept
        queryset.salary = salary
        queryset.bonus = bonus
        queryset.phone = phone
        queryset.role = role
        if img:
            queryset.img=img
        queryset.save()
        return redirect("/view_emp/")
    context={'employee':queryset}
    return render(request,'update_emp.html',context)

def see_emp(request,id):
    queryset=Employee.objects.get(id=id)
    context={'employee':queryset}
    return render(request, 'see_emp.html',context)  


def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            return redirect('/login/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'INVALID CREDENTIALS')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/view_emp/')
        

    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username Already Taken.')
            return redirect('/register/')




        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account Created Successfully.')
        return redirect('/register')
    return render(request,'register.html')
