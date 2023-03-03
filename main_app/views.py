from django.shortcuts import render
from .models import Finch

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

    return render(request, 'finches/detail.html', {'finch': finch})