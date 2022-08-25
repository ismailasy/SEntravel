from django.shortcuts import get_object_or_404, render
from .models import Voyage,Excursion,Reservation,Client,Destination
from .forms import ClientForm,ParagraphErrorList
from django.db import transaction
# Create your views here.
# la premiere vue index affiche la page d'accueil de notre site avec les destinations.
def index(request):
    destinations =Destination.objects.all()
    context = {'destinations':destinations}
    return render(request,'voyage/index.html',context)

#Cette vue affiche toutes les voyages que nous proposons

def listing(request):
    voyages = Voyage.objects.all()
    context = {'voyages':voyages}
    return render(request,'voyage/list.html',context)

#Cette vue nous permet de voir les detail d'un voyage avec les differentes excurtions qui le compose
@transaction.atomic
def detail_voyage(request,voyage_id):
    voyage = get_object_or_404(Voyage,pk=voyage_id)
    excurtions_nom =" ".join([excurtion.nom for excurtion in voyage.excursions.all()])
    context = {
        'voyage_nom':voyage.nom,
        'excurtions_nom':excurtions_nom,
        'voyage_id':voyage.id,
        'voyage_prix':voyage.prix,
        'voyage_pays':voyage.destination,
        'voyage_duree':voyage.duree,
        'thumbnail':voyage.photo   
    }
    if request.method == 'POST':
        form = ClientForm(request.POST,error_class=ParagraphErrorList)
        if form.is_valid():
            prenom = form.cleaned_data['prenom']
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['tel']
            

            client = Client.objects.filter(email=email)
            if not client.exists():
                client = Client.objects.create(
                    prenom =prenom,
                    nom= nom,
                    email = email,
                    tel = telephone
                )
                client.save()
            else:
                client = client.first()
            voyage = get_object_or_404(Voyage,id=voyage_id)
            reservation = Reservation.objects.create(
                client = client,
                voyage = voyage
            )
            reservation.save()
            context = {
                'voyage_nom':voyage.nom
            }
            return render(request, 'voyage/merci.html',context)
        else:
            context['errors'] = form.errors.items()
    else:
        form = ClientForm()  

    context['form'] =form
    return render(request,'voyage/detail_voyage.html',context)

# Cette vu permet de faire une recherche d'un voyage

def search(request):
    query = request.GET.get('query')
    if not query:
        voyages = Voyage.objects.all()
    else:
        # rechercher par le nom du voyage.
        voyages = Voyage.objects.filter(nom__icontains=query)
    
    context ={
        'voyages':voyages
    }

    return render(request,'voyage/search.html',context)

