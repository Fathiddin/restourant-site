from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from .models import Product, Category, CardProduct, Cart, Album, Order
# Create your views here.


def home(request):
    category = Category.objects.all()
    all_product = Product.objects.all()
    albums = Album.objects.all()
    
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create() # yangi cart object hosil qilish
        request.session['user_cart_id'] = cart.id
    
    context = {
        'categorys': category,
        'all_products': all_product,
        'cart': cart,
        'albums': albums
    }
    return render(request, 'index.html', context)

def menu(request):
    category = Category.objects.all()
    all_product = Product.objects.all()
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create() # yangi cart object hosil qilish
        request.session['user_cart_id'] = cart.id
    
    context = {
        'categorys': category,
        'all_products': all_product,
        'cart':cart
    }
    return render(request, 'menu.html', context)

def about(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create() # yangi cart object hosil qilish
        request.session['user_cart_id'] = cart.id
    return render(request, 'about.html', {'cart':cart})

def message(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create() # yangi cart object hosil qilish
        request.session['user_cart_id'] = cart.id
    
    return render(request, 'book.html', {'cart':cart})


def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create() # yangi cart object hosil qilish
        request.session['user_cart_id'] = cart.id
        print(cart)
    return cart


class CartView(TemplateView):
    template_name = "cart.html"
    
    def get(self, request):
        # print(type(request.session))
        # print(dir(request.session))
        cart = cart_init(request)
        return render(request, self.template_name, {"cart":cart})
     
import json
def add_to_cart(request):
    data = json.loads(request.body)
    # print(data)
    cart = cart_init(request)
    status = cart.add(product_id=data.get("product_id"), qty=data.get("qty"))
    if status.get("done"):
        return JsonResponse({"status":"added"})
    else:
        return JsonResponse({"status":"notadded"})
    

def add_to_cart_menu(request):
    data = json.loads(request.body)
    # print(data)
    cart = cart_init(request)
    status = cart.add(product_id=data.get("product_id"), qty=data.get("qty"))
    if status.get("done"):
        return JsonResponse({"status":"added"})
    else:
        return JsonResponse({"status":"notadded"})
    

def deleteItem(request,product_id,qty):
    cart = cart_init(request)
    cart.deleteItem(product_id,qty)
    return redirect('main:cart')


def complated(request):
    return render(request, 'complated.html')

class CheckoutView(View):
    def get(self, request):
        cart = cart_init(request)
        return render(request, 'order.html', {'cart': cart})

    def post(self, request):
        data = request.POST.dict()
        cart = cart_init(request)
        del data['csrfmiddlewaretoken']
        request.session['user_cart_id'] = None
        Order.objects.create(cart=cart, **data)
        return redirect('/complated/')