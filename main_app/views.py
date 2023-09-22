from django.shortcuts import render

finches = [
  {'name': 'Bells', 'species': 'crossbills', 'description': ' a large head, males are a distinctive brick-red ', 'age': 3},
  {'name': 'Goldy', 'species': 'goldfinch', 'description': 'highly coloured finch with a bright red face and yellow wing patch.', 'age': 2},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
 
def finches_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })