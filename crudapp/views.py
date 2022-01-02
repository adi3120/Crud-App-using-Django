from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# Create your views here.
from .forms import dataForm
from .models import dataModel

def create_view(request):
	context={}
	form =dataForm(request.POST or None)
	if form.is_valid():
		form.save()
	context['form']=form
	return render(request,'crudapp/create_view.html',context)

def list_view(request):
	context={}
	
	dataset=dataModel.objects.order_by('-id')[:]
	# context["dataset"]=dataModel.objects.all()
	context["dataset"]=dataset

	return render(request,'crudapp/list_view.html',context)

def detail_view(request,data_id):
	data=get_object_or_404(dataModel,id=data_id)
	context={"data":data}
	return render(request,'crudapp/detail_view.html',context)

def update_view(request,data_id):
	obj=get_object_or_404(dataModel,id=data_id)
	form=dataForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/crudapp/"+str(data_id))

	context={
		"form":form
	}

	return render(request,"crudapp/update_view.html",context)

def delete_view(request,data_id):
	obj=get_object_or_404(dataModel,id=data_id)
	context={
		"text":obj.title
	}
	if request.method=="POST":
		obj.delete()


		return HttpResponseRedirect("/crudapp/list")
	return render(request,'crudapp/delete_view.html',context)

