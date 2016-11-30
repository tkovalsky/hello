from django.shortcuts import render, redirect
from collection.forms import ThingForm
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

def edit_thing(request, slug):
    thing=Thing.objects.get(slug=slug)
    form_class = ThingForm

    if request.method == 'POST':
        # grab the data from the submitted form and apply
        # the form
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
	    #save the new data
            form.save()
            return redirect('thing_detail', slug=thing.slug)
	#other just create the form
    else:
        form = form_class(instance=thing)

	#and render the template
    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,})

def browse_by_name(request, initial=None):
    if initial:
        things = Thing.objects.filter(name__istartswith=initial)
        things = things.order_by('name')
    else:
        things = Thing.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'things': things,
        'initial': initial,
    })
