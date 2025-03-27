from django.shortcuts import render
from .models import Bird, Location, Order

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