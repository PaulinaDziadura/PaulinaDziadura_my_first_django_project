from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import random
from django.views import View
from django_app.models import Game


def main(request):
    page ="""
    <p><a href='/hello/?name=Jan'>Hello Jan </a></p>
    <p><a href='/add/?a=2.5&b=3.5'>suma 2.5 i 3.5  </a> </p>
    <p><a href='/brothers/?name=Jan&name=Adam&name=Iwan'>Bracia</a></p>
    <p><a href='/fibonacci/?n=20'>fibonacci 20</a></p>
    <p><a href='/multiply/?n=3'>mnożenie przez 3 </a></p>
    <p><a href='/game_guess/'>Zagraj w grę</a></p>
    <p><a href='/article/1'>Pierwszy artykuł</a></p>
    <p><a href='/greetings/Jan/5'>Wielokrotne przywitanie</a></p>
    <p><a href='/calc/7/multiply/4'>Mnożenie 7 i 4</a></p>
    <p><a href='/calc/7/divide/4'>Dzielenie 7 i 4</a></p>
    <p><a href='/calc/7/plus/4'>Dodawanie 7 i 4</a></p>
    <p><a href='/calc/7/minus/4'>Odejmowanie 7 i 4</a></p>
    <p><a href='/calc/7/abc/4'>Nieprawidłowa operacja</a></p>
    <p><a href='/random_generator/3/50'>Losowanie liczby z zakresu 3:50</a></p>
    <p><a href='/random_generator/1/6/3'>Rzut kością 3</a></p>
    <p><a href='/form'>Formularz</a></p>
    <p><a href='/login'>Logowanie</a></p>
    <p><a href='/add_product'>Dodawanie produktów</a></p>
    <p><a href='/car'>Wypożyczalnia samochodów</a></p>
    <p><a href='/login_class'>Logowanie Klasy</a></p>
    """
    return HttpResponse(page)


def hello(request):
    name = request.GET.get("name", "nieznajomy")
    return HttpResponse("Witaj " + name)


def add(request):
    a = request.GET.get("a", 0)
    b = request.GET.get("b", 0)
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return HttpResponse("Błędne dane")
    return HttpResponse(a + b)


def brothers(request):
    name_list = request.GET.getlist("name", "")
    page = ""
    for name in name_list:
        page += f"<p>{name}</p>"
    return HttpResponse(page)


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n > 1:
        return fibo(n - 1) + fibo(n - 2)


def fibonacci(request):
    n = request.GET.get("n")
    n = int(n)
    page = "<ol>"
    for i in range(n):
        page += f"<li>{fibo(i)}</li>"
    page += "</ol>"
    return HttpResponse(page)


def multiply(request):
    n = int(request.GET.get("n"))
    page = "<table>"
    for i in range(1, n + 1):
        page += "<tr>"
        for j in range(1, n + 1):
            page += f"<td>{i * j}</td>"
        page += "</tr>"
    page += "</table>"
    return HttpResponse(page)


number = 10


def game_guess(request):
    message = ""
    page = ""
    try:
        guess = request.GET.get("guess")
        guess = int(guess)
        if guess == number:
            message = "Zgadłeś"
        elif guess > number:
            message = "Twoja liczba jest za duża"
        elif guess < number:
            message = "Twoja liczba jest za mała"
    except:
        pass
    page += f"""
    <form> <input name='guess' placeholder= 'podaj liczbę(1-100)'> </form>  {message}
    """
    return HttpResponse(page)


def article(request, id):
    if id == 1:
        return HttpResponse("To jest treść pierwszego artykułu")
    elif id == 2:
        return HttpResponse("To jest treść drugiego artykułu")
    elif id == 3:
        return HttpResponse("To jest treść trzeciego artykułu")
    else:
        return HttpResponse("Brak artykułu o podanym id")


def greetings(request, name, repeat):
    return HttpResponse(f"Witaj {name * repeat}")


def calc(request, number_a, operation, number_b):
    try:
        number_a = float(number_a)
        number_b = float(number_b)
    except ValueError:
        return HttpResponse("Nieprawidłowe dane")
    if operation == "plus":
        sum = number_a + number_b
        return HttpResponse(f"{number_a} + {number_b} = {sum}")
    elif operation == "minus":
        diff = number_a - number_b
        return HttpResponse(f"{number_a} - {number_b} = {diff}")
    elif operation == "multiply":
        mult = number_a * number_b
        return HttpResponse(f"{number_a} * {number_b} = {mult}")
    elif operation == "divide":
        div = number_a / number_b
        return HttpResponse(f"{number_a} : {number_b} = {div}")
    else:
        return HttpResponse("Nie mogę wykonać tej operacji")


def random_generator(request, min, max, throw=1):
    result = 0
    for i in range(throw):
        result += random.randint(min, max)
    return HttpResponse(f"Losowa liczba to:{result}")


def show_template(request):
    names = ["Ala", "Ela", "Iwona", "Beata"]
    context = {
        "message": "To jest wiadomość",
        "names": names
    }
    return render(request, "django_app/index.html", context)


def fizz_buzz(request):
    n = int(request.GET.get("n", 0))
    data = []
    number_1 = 3
    number_2 = 5
    for element in range(1,n+1):
        if element % (number_1 * number_2) == 0:
            data.append("FizzBuzz")
        elif element % number_2 == 0:
            data.append("Buzz")
        elif element % number_1 == 0:
            data.append("Fizz")
        else:
            data.append(element)
    context = {
        "data": data,
        "element": element
    }
    return render(request, "django_app/fizz_buzz.html", context)

def multiply (request):
    n = int(request.GET.get("n"))
    elements = range(1, n + 1)
    context = {
        "elements": elements
    }
    return render(request, "django_app/multiply.html", context)


def form(request):
    if request.method == 'GET':
        return render(request, 'django_app/form.html')

    if request.method == 'POST':
        return HttpResponse("metoda POST wiadomość:" + request.POST.get("message"))

def login_user(request):
    if request.method == 'GET':
        return render(request, 'django_app/login.html')
    if request.method == 'POST':
        user = request.POST.get("user", "")
        password = request.POST.get("password", "")
        if user == "Admin" and password == "Tajne123":
            return HttpResponse("Witaj Admin" )
        else:
            message = "Zły login lub hasło"
        return redirect("/login?message=" + message)



products = {}
def add_product(request):
    if request.method == 'GET':
        return render(request, 'django_app/add_product_form.html')
    if request.method == 'POST':
        product = request.POST.get("product", "")
        price = request.POST.get("price","")
        products[product] = price
        return redirect("/product/show")

def product_show(request):
    context = {
        "products":products
    }
    return render(request, "django_app/product_show.html", context)


class TestView(View):
    def get (self, request):
        return HttpResponse("Metoda get z klasy widoku")
    def post (self,request):
        return HttpResponse("Metoda post z klasy widoku")

class ShowTestView(View):
    def get (self, request):
        return render(request, "django_app/test.html")



class PizzaView(View):
    def get (self, request):
        return render (request, "django_app/pizza.html")
    def post (self, request):
        choice = request.POST.getlist("choice")
        return HttpResponse(f"Wybrałeś: {choice}" )

class CarView(View):
    def get(self, request):
        return render(request, "django_app/car.html")
    def post (self, request):
        car = request.POST.getlist("car")
        return HttpResponse(f"Wybrałeś:{car}")

class LogView(View):
    def get (self,request):
        return render (request, "django_app/login_class.html")
    def post (self, request):
        user = request.POST.get("user", "")
        password = request.POST.get("password", "")
        if user == "Admin" and password == "Tajne123":
            return HttpResponse("Witaj Admin")
        else:
            message = "Zły login lub hasło"
        return redirect("/login_class/?message=" + message)


class GameAdd(View):
    def get (self,request):
        message = "Dodaj grę"
        return render (request, "django_app/game_form.html", {"message":message})
    def post(self,request):
        title = request.POST.get("title")
        publisher = request.POST.get("publisher")
        description = request.POST.get("description")
        price = request.POST.get("price")

        game = Game.objects.create(title=title,
                        publisher=publisher,description=description,price=price)
        return redirect ("/game/")
    # return HttpResponse(str([book.pk, title,publisher, description, page_count,price]))


def game_list(request):
    games = Game.objects.all()
    return render (request, "django_app/game_list.html", {"games": games})

class GameEdit(View):
    def get(self,request, pk):
        game = Game.objects.get(pk=pk)
        message = "Zapisz zmiany"
        return render (request, "django_app/game_form.html", {"game":game, "message":message})
    def post (self,request, pk):
        game = Game.objects.get(pk=pk)
        title = request.POST.get("title")
        publisher = request.POST.get("publisher")
        description = request.POST.get("description")
        price = request.POST.get("price")
        game.title = title
        game.publisher = publisher
        game.description = description
        game.price = price
        game.save()
        return redirect ("/game/")


class GameDelete(View):
    def get(self,request,pk):
        game = Game.objects.get(pk=pk)
        return render(request, "django_app/game_delete.html",
                      {"game":game})

    def post(self,request, pk):
        delete = request.POST.get("delete")
        if delete is not None:
            game = Game.objects.get(pk=pk)
            game.delete()
        return redirect("/game/")

