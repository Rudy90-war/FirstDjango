from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

Creator = {
    "Имя":"Максим",
    "Отчество": "Александрович",
    "Фамилия": "Рудковский",
    "телефон": "8-923-600-01-02",
    "email": "rudy@mail.ru"
}


items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]




def home(request):
   
    context = {
        "name": "Rudkovsky Max",
        "email": "max_mail@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
    text = f"""
    Имя: <b>{Creator["Имя"]}</b><br>
    Отчество: <b>{Creator["Отчество"]}</b><br>
    Фамилия: <b>{Creator["Фамилия"]}</b><br>
    телефон: <b>{Creator["телефон"]}</b><br>
    email: <b>{Creator["email"]}</b><br>
    """
    return HttpResponse(text)

def item(request, item_id):
    for item in items:
        if item['id'] == item_id:
            text = f"""
            <h2> Имя: {item["name"]}<h2>
            <p>  Количество: {item['quantity']} </p>
            <p>  <a href = "/items"> Назад к списку товаров </a>
             """
            return HttpResponse(text)
        
    return HttpResponse(f"Not found")

def getitems(request):
    text = "<h2> Список товаров <h2>"
    for item in items:
        text += f""" <li><a href="/item/{item["id"]}"> {item["name"]} <li> """
    text += "</ol>"
    return HttpResponse(text)


    
