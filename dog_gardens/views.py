from django.shortcuts import render
from .models import Doggarden
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


@login_required(login_url='/accounts/login')
def dog_garden_list(request):
    gardens = Doggarden.objects.all().order_by('name')
    return render(request,'dog_gardens/dog_gardens.html',{'gardens':gardens})


def garden_details(request, name):
    garden = Doggarden.objects.get(name = name)
    return render(request,'dog_gardens/garden-details.html',{'garden': garden})