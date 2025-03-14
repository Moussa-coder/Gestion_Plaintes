from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ProblemeForm
from .models import Probleme
from django.shortcuts import render, get_object_or_404



def home(request):
    return render(request,'home.html')

def signaler_probleme(request):
    if request.method == 'POST':
        form = ProblemeForm(request.POST)
        if form.is_valid():
            probleme = form.save(commit=False)
            probleme.auteur = request.user
            probleme.save()
            return redirect('liste_problemes')  # Redirige vers la liste des problèmes
    else:
        form = ProblemeForm()
    return render(request, 'problemes/signaler_probleme.html', {'form': form})

def liste_problemes(request):
    problemes = Probleme.objects.all()
    return render(request, 'problemes/liste_problemes.html', {'problemes': problemes})

def detail_probleme(request, probleme_id):
    probleme = get_object_or_404(Probleme, pk=probleme_id) 
    context = {'probleme': probleme}
    return render(request, 'detail_probleme.html',context)

def nouveau_probleme(request):
    return render(request, 'problemes/nouveau_probleme.html')

def traitement_probleme(request):
    # Logique de traitement à ajouter ici
    return render(request, 'traitement_probleme.html')







# Create your views here.
