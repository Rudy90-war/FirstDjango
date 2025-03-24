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





def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)


def about(request):
    text = f"""
    Имя: <b>{Creator["Имя"]}</b><br>
    Отчество: <b>{Creator["Отчество"]}</b><br>
    Фамилия: <b>{Creator["Фамилия"]}</b><br>
    телефон: <b>{Creator["телефон"]}</b><br>
    email: <b>{Creator["email"]}</b><br>
    """
    return HttpResponse(text)