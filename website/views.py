from django.shortcuts import render
import datetime


# Create your views here.

def home_page_view(request):
    context = {
        'data': datetime.datetime.now(),
    }
    return render(request, 'website/home.html', context)


def pagina1_page_view(request):
    context = {
        'clube': "Sporting Clube de Portugal"
    }
    return render(request, 'website/pagina1.html', context)


def pagina2_page_view(request):
    campeoes = ["Adán", "Luís Maximiano", "Pedro Porro", "João Pereira", "Gonçalo Inácio", "Coates", "Feddal", "Neto",
                "Eduardo Quaresma", "Nuno Mendes", "Antunes", "Matheus Reis", "Borja", "Palhinha", "Dário Essugo",
                "Matheus Nunes", "João Mário", "Daniel Bragança", "Wendel", "Pedro Gonçalves", "Gonzalo Plata",
                "Bruno Tabata", "Nuno Santos", "Jovane", "Vietto", "Tiago Tomás", "Paulinho", "Sporar"]
    context = {
        'treinador': "Rúben Amorim",
        'listaDeCampeoes': campeoes,
        'nCampeoes': len(campeoes)
    }
    return render(request, 'website/pagina2.html', context)
