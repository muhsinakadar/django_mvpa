from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Staff

def StaffRegistration(request):
    AllData=Staff.objects.all()
    if request.method=="POST":
        firstName=request.POST.get("txtFirstName")
        lastName=request.POST.get("txtLastName")
        position=request.POST.get("txtPosition")
        age=request.POST.get("txtAge")
        Data=Staff()  #Object Creation
        Data.FirstName=firstName
        Data.LastName=lastName
        Data.Position=position
        Data.Age=age
        Data.save()
        return render(request,"DBWork/Staff.html",{"RecordSet":AllData})
    else:
        return render(request,"DBWork/Staff.html",{"RecordSet":AllData})

def DeleteData(request,pk):
    Data=Staff.objects.get(id=pk)
    Data.delete()
    return redirect("SaveStaff")

def EditData(request,pk):
    if request.method=="POST":

        firstName=request.POST.get("txtFirstName")
        lastName=request.POST.get("txtLastName")
        position=request.POST.get("txtPosition")
        age=request.POST.get("txtAge")

        Data=Staff.objects.get(id=pk)  
        
        Data.FirstName=firstName
        Data.LastName=lastName
        Data.Position=position
        Data.Age=age
        Data.save()
        return redirect("SaveStaff")
    else:
        Data=Staff.objects.get(id=pk)
        return render(request,"DBWork/EditStaff.html",{"Data":Data})


    