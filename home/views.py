from django.shortcuts import render

from . models import House

from django.views.generic import DetailView

from django.views.generic.list import ListView


class home_view(ListView):
    model = House
    paginate_by = 3
    template_name = 'home/home.html'

class for_rent_view(ListView):
    model = House
    paginate_by = 12
    template_name = 'home/for_rent.html'

    def get_queryset(self):
        queryset = House.objects.filter(category__startswith="For Rent")
        return queryset

class for_sale_view(ListView):
    model = House
    paginate_by = 12
    template_name = 'home/for_sale.html'

    def get_queryset(self):
        queryset = House.objects.filter(category__startswith="For Sale")
        return queryset

class favourite_view(ListView):
    model = House
    paginate_by = 12
    template_name = 'home/favourites.html'

def about(request):
    return render(request, 'home/about.html', {})

def contact(request):
    return render(request, 'home/contact.html', {})

class house_details(DetailView):
    model = House
    template_name = 'home/house_details.html'
