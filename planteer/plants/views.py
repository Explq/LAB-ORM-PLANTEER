from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Plant
from .forms import PlantForm

def all_plants(request):
    category_filter = request.GET.get('category', '')
    is_edible_filter = request.GET.get('is_edible', None)
    query = request.GET.get('query', '')


    plant_list = Plant.objects.all()

    if category_filter:
        plant_list = plant_list.filter(category=category_filter)

    if is_edible_filter is not None:

        plant_list = plant_list.filter(is_edible=is_edible_filter == 'true')

    if query:
        plant_list = plant_list.filter(name__icontains=query)


    paginator = Paginator(plant_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'plants/all_plants.html', {
        'page_obj': page_obj,
        'category_filter': category_filter,
        'is_edible_filter': is_edible_filter,
        'query': query,
    })



def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant.id)[:3]

    return render(request, 'plants/plant_detail.html', {
        'plant': plant,
        'related_plants': related_plants
    })

def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = PlantForm()

    return render(request, 'plants/add_plant.html', {'form': form})
def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)

    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plants:plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)

    return render(request, 'plants/update_plant.html', {
        'form': form,
        'plant': plant
    })

def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)

    if request.method == 'POST':
        plant.delete()
        return redirect('plants:all_plants')

    return render(request, 'plants/delete_plant.html', {
        'plant': plant
    })

def search_plants(request):
    query = request.GET.get('query', '')
    if query:
        plants = Plant.objects.filter(name__icontains=query)
    else:
        plants = Plant.objects.none()

    paginator = Paginator(plants, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'plants/search_plants.html', {
        'page_obj': page_obj,
        'query': query
    })
