from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.mascota.models import Mascota

from apps.mascota.form import MascotaForm
# Create your views here.

def index(request):
  return HttpResponse("index de Mascota")

def  mascota_list(request):
  mascota = Mascota.objects.all().order_by('id')
  contexto={'mascotas': mascota}
  return render(request,'mascota/mascota_list.html',contexto)
  

def mascota_view(request):
  if request.method =='POST':
    form= MascotaForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('mascota_listar')
  else:
    form= MascotaForm()
  return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_edit(request,id_mascota):
  mascota=Mascota.objects.get(id=id_mascota)
  if request.method=='GET':
    form=MascotaForm(instance=mascota)
  else:
    form= MascotaForm(request.POST, instance=mascota)
    if form.is_valid():
      form.save()
    return redirect('mascota_listar')
  return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_delete(request,id_mascota):
  mascota =Mascota.objects.get(id=id_mascota)
  if request.method =='POST':
    mascota.delete()
    return redirect('mascota_listar')
  return render(request,'mascota/mascota_delete.html',{mascota:'mascota'})