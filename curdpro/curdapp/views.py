from django.shortcuts import render
from .models import ProductData
from .forms import ProductForm,UpdateForm,DeleteForm
# Create your views here.
from django.http.response import HttpResponse

def homeview(request):
    return render(request,'curdhome.html')

def inserting(request):
    if request.method=="POST":
        pform=ProductForm(request.POST)
        if pform.is_valid():
            vpid=request.POST.get('fproduct_id','')
            vpname=request.POST.get('fproduct_name','')
            vpcost=request.POST.get('fproduct_cost','')
            vpcolor=request.POST.get('fproduct_color','')
            vpclass=request.POST.get('fproduct_class','')
            vpproducts=request.POST.get('fnumber_of_products','')
            vcname=request.POST.get('fcustomer_name','')
            vmobile=request.POST.get('fmobile_number','')
            vemail=request.POST.get('femail','')
            data=ProductData(
                mproduct_id=vpid,
                mproduct_name=vpname,
                mproduct_cost=vpcost,
                mproduct_color=vpcolor,
                mproduct_class=vpclass,
                mnumber_of_products=vpproducts,
                mcustomer_name=vcname,
                mmobile_number=vmobile,
                memail=vemail)
            data.save()
        pform=ProductForm()
        return render(request,'curdinserting.html',{'pform':pform})
    else:
        pform=ProductForm()
        return render(request,'curdinserting.html',{'pform':pform})

def retrieving(request):
    rdata=ProductData.objects.all()
    return render(request,'curdretrieving.html',{'rdata':rdata})

def updating(request):
    if request.method=="POST":
        uform=UpdateForm(request.POST)
        if uform.is_valid():
            upid=request.POST.get('ufproduct_id','')
            upcost=request.POST.get('ufproduct_cost','')
            uprod_id=ProductData.objects.filter(mproduct_id=upid)
            if not uprod_id:
                return HttpResponse("<h1>Data is Not Available</h1>")
            else:
                uprod_id.update(mproduct_cost=upcost)
                uform=UpdateForm()
                return render(request,'curdupdating.html',{'uform':uform})
        else:
            return HttpResponse("Invalid Form")
    else:
        uform=UpdateForm()
        return render(request,'curdupdating.html',{'uform':uform})
def deleting(request):
    if request.method=="POST":
        dform=DeleteForm(request.POST)
        if dform.is_valid():
            dpid=request.POST.get('dfproduct_id','')
            dprod_id=ProductData.objects.filter(mproduct_id=dpid)
            if not dprod_id:
                return HttpResponse("<h1>Data is Not Availablle</h1>")
            else:
                dprod_id.delete()
                dform=DeleteForm()
                return render(request,'curddeleting.html',{'dform':dform})
        else:
            return HttpResponse("<H1>Form is Invalid</H1>")
    else:
        dform=DeleteForm()
        return render(request,'curddeleting.html',{'dform':dform})

