from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count, Min, Sum, Max
from .models import Mobile, Comment
from .forms import ProducerForm
import json


producerToSearch = ''

def home(req):
    return render(req, 'home.html', {'page_title': 'Mobiles'})

#sa - ispred naziva kolone, sort desc
#bez - ispred naziva kolone, sort asc     

def min_prices(request):
    return render(request, 'min-prices.html')

def minimum(request):
    labels = []
    data = []

    queryset = Mobile.objects.all().order_by('price')[:10]
    for mob in queryset:
        labels.append(mob.model)
        data.append(mob.price)   

    print(labels)
    print(data)

    return JsonResponse(data={
        'labels': labels,
        'data': data
    })    

def max_prices(request):
    return render(request, 'max-prices.html')

def maximum(request):
    labels = []
    data = []  

    queryset = Mobile.objects.all().order_by('-price')[:10]
    for mob in queryset:    
        labels.append(mob.model)
        data.append(mob.price)   

    return JsonResponse(data={
        'labels': labels,
        'data': data
    })      

def max_comments_for_phone(request):
    labels = []
    data = []  
    models = []

    queryset = Comment.objects.values('mobile').annotate(num_phones=Count('mobile')).order_by('-num_phones')[:5]
    print(queryset)

    for mob in queryset:
        labels.append(mob.get('mobile'))
        data.append(mob.get('num_phones'))   

    for n in labels:
        model = Mobile.objects.get(id=n)
        models.append(model.model)      

    return render(request, 'max-comments.html', {
        'labels': json.dumps(models),
        'data': json.dumps(data),
    })    

def top_active_users(request):
    labels = []
    data = []  

    queryset = Comment.objects.values('username').annotate(num_users=Count('username')).order_by('-num_users')[:5]
    print(queryset)

    for mob in queryset:
        labels.append(mob.get('username'))
        data.append(mob.get('num_users'))        

    return render(request, 'top-active-users.html', {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    })

def producerSearch(req):
    if req.method == 'POST':
        form = ProducerForm(req.POST)

        if form.is_valid():
            phones = Mobile.objects.filter(producer=form.cleaned_data['producer'])
            print(phones)
            global producerToSearch
            producerToSearch = form.cleaned_data['producer']
            print(producerToSearch)
            return redirect('baza:modelsByProducer')
        else:
            return redirect('baza:producerSearch')
    else:
        mob = Mobile(producer="")
        form = ProducerForm(instance=mob)
        return render(req, 'producer-search.html', {'form': form })

def modelsByProducer(request):
    return render(request, 'models-by-producer.html')
 
def models_chart(request):
    labels = []
    data = []

    queryset = Mobile.objects.values('model').annotate(price=Sum('price')).order_by('-price').filter(producer=producerToSearch)
    for entry in queryset:
        labels.append(entry['model'])
        data.append(entry['price'])
     
    return JsonResponse(data={
        'labels': labels,
        'data': data,
        'marka': producerToSearch
    }) 

def min_max_for_producer(request):
    labels = []
    data = []

    phones = Mobile.objects.filter(producer=producerToSearch)
    queryset =phones.aggregate(Max('price'), Min('price'))
    
    data.append(queryset.get('price__max'))
    data.append(queryset.get('price__min'))
    
    labels.append('Max price')
    labels.append('Min price')  

    return render(request, 'min-max-producer.html', {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    })   

def searchProducerMinMax(req):
    if req.method == 'POST':
        form = ProducerForm(req.POST)

        if form.is_valid():
            phones = Mobile.objects.filter(producer=form.cleaned_data['producer'])
            print(phones)
            global producerToSearch
            producerToSearch = form.cleaned_data['producer']
            print(producerToSearch)
            return redirect('baza:min_max_for_producer')
        else:
            return redirect('baza:searchProducerMinMax')
    else:
        mob = Mobile(producer="")
        form = ProducerForm(instance=mob)
        return render(req, 'min-max-search.html', {'form': form })           
                     
