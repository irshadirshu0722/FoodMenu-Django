from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .form import Itemform
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

def index(request):
    return HttpResponse("Hello World")


# Item list
def list(request):
    item_list = Item.objects.all()
    # template=loader.get_template("food/index.html")
    
    context={
        'item_list':item_list

    }
    return render(request,'food/index.html',context=context)
    # return HttpResponse(template.render(context,request))

class ListClassViews(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'
    


# Show detail of item
def detail(request,pk):
    item_detail = Item.objects.get(pk=pk)
    context={
        'object':item_detail,
        'user':str(item_detail.user_name),
        'author':str(request.user.username)
    }
    
    
    return render(request,'food/detail.html',context=context)
    # return HttpResponse(f"this is item no {id}")

class DetailClassView(DetailView):
    model=Item
    template_name = 'food/detail.html'

# Create item 
def create_item(request):
    form = Itemform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:list')
    context = {
        'form':form
    }
    return render(request,'food/add_item.html',context=context)

class CreateItemClassView(CreateView):
    model = Item
    form_class  =Itemform
    
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        
        return super().form_valid(form)
    template_name = 'food/add_item.html'

# Edit Item
def edit_item(request,id):
    item = Item.objects.get(id=id)

    form = Itemform(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:list')
    
    
    return render(request,'food/edit_item.html',context={"form":form})

class UpdateItemClassView(UpdateView):
    model = Item
    form_class  = Itemform
    template_name = 'food/edit_item.html'
    success_url ="/food/"

# Delete Item
def delete_item(request,id):
    item = Item.objects.get(id=id)
   
    if request.method   == 'POST' :

        item.delete()
    
        return redirect('food:list')
    return render(request,'food/delete_item.html',context={"item":item})

class DeleteItemClassView(DeleteView):
    model = Item
    template_name = 'food/delete_item.html'  
    success_url = '/food/'
    


