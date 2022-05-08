from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from produit.models import Produit
from personne.models import Personne
from commande.models import Commande


def index(request):
    produit_object = Produit.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        produit_object = Produit.objects.filter(nomProduit__icontains=item_name)
    paginator = Paginator(produit_object, 10)
    page = request.GET.get('page')
    produit_object = paginator.get_page(page)
    return render(request, 'index.html', {'produit_object': produit_object})

def detail(request, id):
    produit_object = Produit.objects.filter(id=id)
    return render(request, 'detail.html', {'produit_object': produit_object})

def checkout(request):
    if request.method == "POST":
        Produit = request.POST.get('Produit')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        referanceCommande = request.POST.get('referanceCommande')
        dateCmd = request.POST.get('dateCommande')
        pe = Personne(nom=nom, prenom=prenom, email=email)
        com = Commande(Produit=Produit, referanceCommande=referanceCommande, dateCmd=dateCmd)
        pe.save()

    return render(request, 'checkout.html')