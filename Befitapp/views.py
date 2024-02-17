from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect,render_to_response,redirect
# def index(request):
#     return render(request,'index.html')
    
def login(request):
     return render(request,'login.html')   

def dietitian(request):
     return render(request,'dietitian.html')   

def healthclub(request):
     return render(request,'healthclub.html')   

def medical(request):
     return render(request,'medical.html')   

def nutrition(request):
     return render(request,'nutrition.html')   

def viewdieti(request):
     return render(request,'viewdieti.html')   
def Registration(request):
     return render(request,'Registration.html')
def Registrationaction(request):
     cursor=connection.cursor()
     un=request.GET['username']
     c=request.GET['contact']
     e=request.GET['email']
     g=request.GET['gender']
     p=request.GET['password']
     cp=request.GET['conpass']
     sql="insert into registration(name,email,contactno,gender,password,conpass)values('%s','%s','%s','%s','%s','%s')"%(un,e,c,g,p,cp)
     cursor.execute(sql)
     return render(request,'Registration.html')
def medicalaction(request):
     cursor=connection.cursor()
     a=request.GET['age']
     h=request.GET['height']
     w=request.GET['weight']
     g=request.GET['gender']
     op=request.GET['yes-no']
     db=request.GET['deabetic']
     bp=request.GET['bp']
     mc=request.GET['medical']
     sql="insert into medical(age,height,weight,gender,operation,deabetic,bp,medicalcontinous)values('%s','%s','%s','%s','%s','%s','%s','%s')"%(a,h,w,g,op,db,bp,mc)
     cursor.execute(sql)
     return render(request,'medical.html') 
def nutritionaction(request):
     cursor=connection.cursor()
     n=request.GET['name']
     a=request.GET['age']
     d=request.GET['details']
     f=request.GET['file']
     e=request.GET['email']
     c=request.GET['contact']
     ad=request.GET['address']
     p=request.GET['password']  
     sql="insert into nutrition(name,age,details,file,email,contactno,address,password)values('%s','%s','%s','%s','%s','%s','%s','%s')"%(n,a,d,f,e,c,ad,p)
     cursor.execute(sql)
     return render(request,'nutrition.html')
def dietitianaction(request):
     cursor=connection.cursor()
     e=request.GET['email']
     p=request.GET['password']
     a=request.GET['age']
     g=request.GET['gender']
     n=request.GET['name']
     sql="insert into dietitian(email,password,age,gender,name)values('%s','%s','%s','%s','%s')"%(e,p,a,g,n)
     cursor.execute(sql)
     return render(request,'dietitian.html')
def healthclub(request):
     return render(request,'healthclub.html')
def healthclubaction(request):
     cursor=connection.cursor()
     cn=request.GET['name']
     ad=request.GET['address']
     pl=request.GET['place']
     ca=request.GET['category']
     cno=request.GET['contact']
     em=request.GET['email']
     pas=request.GET['password']
     sql="insert into club(name,address,place,category,contactno,email,password)values('%s','%s','%s','%s','%s','%s','%s')"%(cn,ad,pl,ca,cno,em,pas)
     cursor.execute(sql)
     return render(request,'healthclub.html')
def viewdiet(request):
     return render(request,'viewdiet.html')
def viewdietaction(request):
     cursor=connection.cursor()
     t=request.GET['time']
     d=request.GET['date']
     dn=request.GET['name']
     dur=request.GET['duration']
     re=request.GET['reason']
     c=request.GET['contact']
     mr=request.GET['medical']
     sql="insert into viewdietitian(time,date,name,duration,reason,contact,medicalrecord)values('%s','%s','%s','%s','%s','%s','%s')"%(t,d,dn,dur,re,c,mr)
     cursor.execute(sql)
     return render(request,'viewdiet.html')

