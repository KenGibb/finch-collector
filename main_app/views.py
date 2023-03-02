from django.shortcuts import render

finches = [
    {'name': 'Terry', 'species': 'American Goldfinch', 'age': '2', 'description': 'Nice gold birdy'},
    {'name': 'Laura', 'species': 'House Finch', 'age': '4', 'description': 'Oh cool woody looking bird with a red head'},
    {'name': 'Bill', 'species': 'Cassia Crossbill', 'age': '1', 'description': 'A bird with a red plumage'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })