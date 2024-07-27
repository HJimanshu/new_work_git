from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.
# def cru(request): this method check the installation of app in project
#     return HttpResponse('hii')

def InsertPageView(request):
    return render(request,"crud/insert.html")
def InsertData(request):
    #Data come from HTML to view
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']
    #Create Object of Model Class
    # Inserting data into table
    newuser=Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)
    
    #After Insert render on show.html
    # return render(request,"crud/show.html")
    return redirect('showpage')

def ShowPage(request):
    #Select * from tablename
    #For Fetching all the data of the table
    all_data = Student.objects.all()
    return render(request,"crud/show.html",{'key1':all_data})

#Edit page view
def Editpage(request,pk):
    #Fetching tha data of particular ID
    get_data = Student.objects.get(id=pk)
    return render(request,"crud/edit.html",{'key2':get_data})
    

#update Data view
def UpdateData(request,pk):
    udata=Student.objects.get(id=pk)
    udata.Firstname=request.POST['fname']  
    udata.Lastname=request.POST['lname']  
    udata.Email=request.POST['email']  
    udata.Contact=request.POST['contact']
    
    #Query for update 
    udata.save()
    #render to show page
    return redirect('showpage')
 
# Delete Data view 
def DeleteData(request,pk):
    ddata=Student.objects.get(id=pk)
    
    #Query for delete
    ddata.delete()
    return redirect('showpage')
    