from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the Finch Model
from .models import Finch



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
 
def finches_index(request):
  finches = Finch.objects.all()
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })

class FinchCreate(CreateView):
   model = Finch
   fields = '__all__'
  
class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['species', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'
