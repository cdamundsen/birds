from django.shortcuts import get_object_or_404, render
#from django.contrib.auth.decorators import login_required
from .models import Detection, Bird, Location, Order

# Create your views here.
def birds_list(request):
    birds = Bird.objects.all().order_by('common_name')
    return render(
        request,
        'merlin/birds_list.html',
        {
            'birds': birds,
        }

    )

def locations(request):
    locations = Location.objects.all().order_by('name')
    return render(
        request,
        'merlin/locations.html',
        {
            'locations': locations,
        }
    )


def orders(request):
    orders = Order.objects.all().order_by('name')
    return render(
        request,
        'merlin/orders.html',
        { 
            'orders': orders,
        }
    )
def bird(request, bird_slug):
    bird = get_object_or_404(
        Bird,
        slug=bird_slug
    )
    detections = bird.detections.all().order_by('date')
    return render(
        request,
        'merlin/bird.html',
        {
            'bird': bird,
            'detections': detections,
        }
    )