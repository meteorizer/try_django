"""view"""
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    print(dict(request.POST))
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('id_new_item', ''),
    })

