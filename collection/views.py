from django.shortcuts import render
from collection.models import Thing

# Create your views here.

def index(request):
    things = Thing.objects.all()
    return render(request, 'index.html', {
        'things': things,
	})

def thing_detail(request, slug):
    #get the objects
    thing = Thing.objects.get(slug=slug)

    #and pass the object to the template
    return render(request, 'things/thing_detail.html', {
        'thing':thing,
    })

    
