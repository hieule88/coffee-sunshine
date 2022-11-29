from django.shortcuts import render
from rest_framework.decorators import api_view
from .backend import get_cart_data
from django.http import HttpResponse
# from pyngrok import ngrok
# ...
# url = ngrok.connect(8000).public_url
# print('Henzy Tunnel URL:', url)
# Create your views here.

dict_drinkimg = {
    "cappuccino" : "cappuccino.png",
    "dứa ép" : "duaep.png",
    "cà phê đen" : "dennongimg.png",
    "cà phê nâu" : "suada.png",
    "bạc sỉu" : "bacsiu.png",
    "cà phê cốt dừa" : "cotdua.png",
    "espresso" : "espresso.png",
    "americano" : "americano.png",
    "cà phê latte" : "icedlatte.png",
    "cà phê mocha" : "caphemocha.png",
    "nước ép dứa mít nha đam" : "nhadamep.png",
    "dừa trái" : "duatrai.png",
    "sinh tố bơ" : "sinhtobo.png",
    "sinh tố bơ sữa dừa hạnh nhân" : "sinhtobo.png",
    "cam nguyên chất" : "camimg.png",
    "trà sen lá nếp" : "senlanep.png",
    "trà đào cam xả" : "daocamxa.png",
    "ô long vải trà" : "olongvai.png",
    "trà bưởi hồng" : "hongtra.png",
    "trà quất mật ong" : "quatmatong.jpg",
    "trà hoa cúc táo xanh" : "cuctaoxanh.jpg",
    "thạch matcha" : "thachmatcha.png",
    "sô cô la hạnh nhân" : "hanhnhan.jpg",
    "sữa chua việt quất" : "vietquat.jpg",
}

@api_view(['GET'])
def cartview(request):
    # cart_items = get_cart_data()

    title = request.GET.get('title') if request.GET.get('title') != None else '' 
    if title == '':
        return render(request, "menu.html")
    size = request.GET.get('size') if request.GET.get('size') != None else ''
    quantity = request.GET.get('quantity') if request.GET.get('quantity') != None else ''
    floor = request.GET.get('floor') if request.GET.get('floor') != None else ''

    cart_items = [
        [
            title.capitalize(), 
            size,
            quantity,
            floor,
        ],
    ]
    
    context = {
        "item": cart_items[0],
        "drinkimage": dict_drinkimg[title],
    }

    response = render(request, "payment.html", context=context)
    return response