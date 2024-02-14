from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("hello")

def home(request):
    return HttpResponse("""
        <body style='background-color: pink;'>
            <h1 style='color: red;'>heading</h1>
            <p>para</p>
        </body>
    """)

def menuitem(request):
    item = "pizza"
    return HttpResponse(f"the item name is {item}")

def menuitems(request):
    items = {
        'Noodles': 'costs Rs. 120',
        'pizza': 'costs Rs. 150',
        'momos': 'costs Rs. 100'
    }
    content = "<h1>The food items are</h1>"
    for item, description in items.items():
        content += f"<h2>{item}</h2><p>{description}</p>"
    return HttpResponse(content)

def greet(request, name):
    return HttpResponse(f"Hello {name}, Welcome to our website")

# def foods(request, food):
#     items = {
#         'Noodles': 'costs Rs. 120',
#         'pizza': 'costs Rs. 150',
#         'momos': 'costs Rs. 100',
#         'cake': 'costs Rs. 250'
#     }
#     content = f"cost of {food} is: {items.get(food, 'Not available')}"
#     return HttpResponse(content)

def add_numbers(request, num1, num2):
    sum = int(num1) + int(num2)
    return HttpResponse(f"The sum of {num1} and {num2} is {sum}")
def add(request):
    value1 = request.GET.get('value1')
    value2 = request.GET.get('value2')
    sum = int(value1)+int(value2)
    return HttpResponse(f"The addition is {sum}")



def calculate(request):

    value1 = request.GET.get('value1', 0)
    value2 = request.GET.get('value2', 0)
    operation = request.GET.get('operation', 'add')

    try:
        
        value1 = float(value1)
        value2 = float(value2)

        if operation == 'add':
            result = value1 + value2
        elif operation == 'subtract':
            result = value1 - value2
        elif operation == 'multiply':
            result = value1 * value2
        elif operation == 'divide':
            
            if value2 != 0:
                result = value1 / value2
            else:
                return HttpResponse("Error: Division by zero is not allowed.")
        else:
            return HttpResponse("Error: Invalid operation.")

        return HttpResponse(f"Result of {operation}({value1}, {value2}) is {result}")

    except ValueError:
        return HttpResponse("Error: Invalid input. Please provide valid numeric values.")

def user_profile(request, username):
    return HttpResponse(f"the usernames is {username}")
def items(request, item_id):
    return HttpResponse(f"the usernames is {item_id}")
def info_view(request, month, year):
    return HttpResponse(f"Info for {month}/{year}")
def post(request, post):
    return HttpResponse(f"the usernames is {post}")
def menu_category(request, category):
    return HttpResponse(f"Category: {category}")

def menu_subcategory(request, category, subcategory):
    return HttpResponse(f"Category: {category}, Subcategory: {subcategory}")


def restro(request):
    items = [{'name':'Pizza', 'cost': 500},
{'name':'Fries', 'cost': 'free'},
{'name':'Momos', 'cost': 80},
{'name':'Chutney', 'cost': 'free'},
{'name':'pasta','cost':70}]
    return render(request, 'restro.html', {'items': items})


def restro(request, item_name):
    item = get_object_or_404(MenuItem, name__iexact=item_name)
    return render(request, 'restro.html', {'item': item})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def food(request):
    items = [
        {'name': 'Burger', 'cost': '₹300', 'details': 'Burger details'},
        {'name': 'Pizza', 'cost': '₹500', 'details': 'Pizza details'},
        {'name': 'Fries', 'cost': '₹200', 'details': 'Fries details'},
        {'name': 'Hot Dog', 'cost': '₹250', 'details': 'Hot Dog details'},
        {'name': 'Chicken Wings', 'cost': '₹400', 'details': 'Chicken Wings details'}
    ]
    return render(request, 'food.html', {'items': items})


def food_detail(request, item_name):
    items = [
        {'name': 'Burger', 'cost': '₹300', 'details': 'Burger details'},
        {'name': 'Pizza', 'cost': '₹500', 'details': 'Pizza details'},
        {'name': 'Fries', 'cost': '₹200', 'details': 'Fries details'},
        {'name': 'Hot Dog', 'cost': '₹250', 'details': 'Hot Dog details'},
        {'name': 'Chicken Wings', 'cost': '₹400', 'details': 'Chicken Wings details'}
    ]
    for item in items:
        if item['name'] == item_name:
            context = {'item': item}
            return render(request, 'food_details.html', context)
    return render(request, '404.html')