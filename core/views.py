from django.shortcuts import render, redirect,get_object_or_404
from .models import Cart, CartItem, Product
from django.contrib.auth.decorators import login_required
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'main.html', {'products': products})

def index(request):
    return render(request, "core/index.html")

def explore(request):
    return render(request, "core/product_list.html")

def about(request):
    return render(request, 'core/about.html')

def recipe_list(request):
    return render(request, 'core/recipe_list.html')


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def remove_from_cart(request, item_id):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(id=item_id, cart=cart)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass 
    
    return redirect('view_cart') 
@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    }) 

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('product_list')


@login_required
def update_cart(request):
    if request.method == 'POST':
        cart, created = Cart.objects.get_or_create(user=request.user)
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')

        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)

            if action == 'increase':
                cart_item.quantity += 1
            elif action == 'decrease' and cart_item.quantity > 1:
                cart_item.quantity -= 1
            elif action == 'decrease' and cart_item.quantity == 1:
                cart_item.delete()  
            elif action == 'remove':
                cart_item.delete()

            if action != 'remove':
                cart_item.save()

        except CartItem.DoesNotExist:
            pass
    return redirect('view_cart') 

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'core/product_detail.html', {'product': product})



