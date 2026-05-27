from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def pratos(request):
    pratos = [
        {"nome": "Bauru",
         "ingredientes": "Pão, ovo, queijo, presunto, carne e salada.",
         "preco": "R$ 10,00",
         "tempo": "10min",
         "imagem": "website/assets/img/portfolio/cabin.png",
        },
        {"nome": "Lasanha",
         "ingredientes": "Macarrão, molho, carne, presunto, queijo.",
         "preco": "R$ 70,00",
         "tempo": "1h30min",
         "imagem": "website/assets/img/portfolio/controller.png",
        },
        {"nome": "Tapioca",
         "ingredientes": "Goma",
         "preco": "R$ 2,50",
         "tempo": "10min",
        },
    ]
    context = {"pratos": pratos}
    return render(request, 'website/pratos.html', context)

def sobre(request):
    return render(request, 'website/sobre.html')
