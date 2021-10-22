from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import shop
from .forms import updateForm


# Create your views here.
def demo(request):
    shops=shop.objects.all()
    return render(request,"home.html",{'shop':shops})
def details(request,shop_id):
    shop_selected=shop.objects.get(id=shop_id)
    return render(request, "details.html", {'shop': shop_selected})
def insert(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        price = request.POST.get('price')
        img = request.FILES['img']
        item=shop(name=name,desc=desc,price=price,img=img)
        item.save()
        print("product added")
    return render(request,"add.html")
def update (request,shop_id):
    shop_modi=shop.objects.get(id=shop_id)
    form=updateForm(request.POST or None,request.FILES,instance=shop_modi)
    if form.is_valid():
        form.save()
        return redirect ('/')
    return render (request,'update.html',{"form":form,'obj':shop_modi})
def delete (request,shop_id):
    if request.method=='POST':
        item=shop.objects.get(id=shop_id)
        item.delete()
        return redirect('/')
    return render (request,'delete.html')