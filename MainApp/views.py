from django.shortcuts import render
from django.http import HttpResponse
from MainApp.models import Item
# Create your views here.




#items = [
#{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#{"id": 7, "name": "Картофель фри" ,"quantity":0},
#{"id": 8, "name": "Кепка" ,"quantity":124},
#]




def home(request):
   
    context = {
        "name": "Rudkovsky Max",
        "email": "max_mail@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
   
    author = {
    "name":"Максим",
    "middle_name": "Александрович",
    "last_name": "Рудковский",
    "phone": "8-923-600-01-02",
    "email": "rudy@mail.ru"
    }
   
    return render(request, "about.html", {"author": author})

def item(request, item_id):
   # for item in items:
    #    if item['id'] == item_id:
     #       text = f"""
     #       <h2> Имя: {item["name"]}<h2>
      #      <p>  Количество: {item['quantity']} </p>
       #     <p>  <a href = "/items"> Назад к списку товаров </a>
        #     """
         #   return HttpResponse(text)
        
  #  return HttpResponse(f"Not found")
  
    item = Item.objects.get(id=item_id)
    if item is not None:
        context = {
            "item": item
        }
        return render(request, "item_page.html", context)
    return HttpResponse(f"Not found")

def getitems(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_ls.html", context)


    
