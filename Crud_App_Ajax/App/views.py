
from json.decoder import JSONDecodeError
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User
from .forms import User_data
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def Home(request):
    form = User_data() 
    data  = User.objects.all()
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        form = User_data(request.POST)
        
        print(form ,"view")
        if form.is_valid():
            
            if request.POST.get('sid'):
                print(request.POST ,"printing from update")

            else:
                obj = form.save(commit=False)
                obj.save()
            if request.is_ajax():
                return JsonResponse(obj.seralize(), status = 201)
                
            form = User_data() 
    return render(request , 'app/home.html' ,context={'form':form , 'data': data })

@csrf_exempt
def delete(request):

   
    if request.method =='POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        obj = User.objects.get(id=body)
        obj.delete()

    return JsonResponse({})

@csrf_exempt
def update(request):
    if request.method =="POST":
        body_unicode = request.body.decode('utf-8')
        body_id = json.loads(body_unicode)
        obj = User.objects.get(pk=body_id)
        data_update = obj.seralize()
        name_up = data_update['name']
        email_up = data_update['email']
        pas_up = data_update['password']
    return JsonResponse(data_update,safe=False)
    

def details_view(request):
    data  = list(User.objects.values())
    return JsonResponse(data ,safe= False)