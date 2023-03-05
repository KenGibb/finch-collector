from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Finch, Toy
from .forms import FeedingForm

# finches = [
#     {'name': 'Terry', 'species': 'American Goldfinch', 'age': '2', 'description': 'Nice gold birdy'},
#     {'name': 'Laura', 'species': 'House Finch', 'age': '4', 'description': 'Oh cool woody looking bird with a red head'},
#     {'name': 'Bill', 'species': 'Cassia Crossbill', 'age': '1', 'description': 'A bird with a red plumage'},
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)

    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form
})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = '__all__'
    ## or I could make it 'description, 'age, 'species'

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

# ToyList
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

# ToyDetail
class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

# ToyCreate
class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    def form_valid(self, form):
        return super().form_valid(form)

# ToyUpdate
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

# ToyDelete
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'