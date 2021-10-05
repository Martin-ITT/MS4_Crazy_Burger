from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    # A view to render the shopping bag page

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    # Add a quantity of the specified product to the shopping bag

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    print("\n POST request from form to add_to_bag:")
    print(request.POST)
    size = None
    drink = ""

    # variable to pass some product data to context.py
    product_data = None

    price = None
    toppings = ""
    topping_charge_medium = 1
    topping_charge_large = 1.5

    # product is pizza
    if 'opt-pizza' in request.POST:
        size = request.POST['opt-pizza']
        if 'opt-topping' in request.POST:
            toppings = "-".join(request.POST.getlist('opt-topping'))
        num_of_toppings = len(request.POST.getlist('opt-topping'))
        print("\n num of toppingd")
        print(num_of_toppings)
        # toppings displayed only if selected
        if num_of_toppings > 0:
            product_data = size + "_pizza_" + toppings + "_" + item_id
        else:
            product_data = size + "_other-pizza_" + toppings + "_" + item_id
        # set price by size plus charge toping if any
        if size == 'small':
            price = request.POST['id-price']
        if size == 'medium':
            price = float(request.POST['id-price-medium']) + (
                topping_charge_medium * num_of_toppings)
        if size == 'large':
            price = float(request.POST['id-price-large']) + float(
                topping_charge_large * num_of_toppings)

    # products with more sizes - not pizza
    if 'opt-size' in request.POST:
        size = request.POST['opt-size']
        if size == 'small':
            price = request.POST['id-price']
        if size == 'medium':
            price = request.POST['id-price-medium']
        if size == 'large':
            price = request.POST['id-price-large']
        product_data = size + '_size_' + drink + "_" + item_id

    # products which can be upgraded to meal
    if 'is-meal' in request.POST:
        size = request.POST['is-meal']
        drink = request.POST['meal-drink']
        product_data = size + '_meal_' + drink + "_" + item_id
        if size == 'meal':
            price = request.POST['id-price-meal']
        else:
            price = request.POST['id-price']

    # product is meal, has sizes or is pizza
    if product_data:
        # is product id already in a bag
        if item_id in list(bag.keys()):
            # exactly same product added
            if product_data in bag[item_id]['product_data'].keys():
                bag[item_id]['product_data'][product_data] += quantity
                messages.success(
                    request, f'{product.name} - {size} - quantity updated.')
            # same id products but different attributes
            else:
                bag[item_id]['product_data'][product_data] = quantity
                bag[item_id]['price'][product_data] = price
                messages.success(
                    request, f'{product.name} - {size} added to bag.')
        # product added for a first time
        else:
            bag[item_id] = {
                'product_data': {product_data: quantity},
                'price': {product_data: price},
                }
            messages.success(
                request, f'{product.name} - {size} added to bag.')
    # products with no extra options
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'{product.name} - quantity updated.')
        else:
            bag[item_id] = quantity
            messages.success(request, f'{product.name} added to bag.')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    # Adjust the quantity of the specified product in the shopping bag

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
        quantity = int(request.POST['quantity'])

    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)

    if quantity > 0 and quantity < 99:
        # product is meal, has sizes or is pizza
        if size:
            # product id already in a bag
            if quantity > 0:
                bag[item_id]['product_data'][size] = quantity
                messages.success(
                    request, f'{product.name} - {size.split("_")[0]} - quantity updated.')
                # problem to get product_data from request.POST
            else:
                del bag[item_id]['product_data'][size]
                messages.success(
                    request, f'{product.name} - {size.split("_")[0]} - removed from bag.')
                if not bag[item_id]['product_data']:
                    bag.pop(item_id)
        # products with no extra options
        else:
            if quantity > 0:
                bag[item_id] = quantity
                messages.success(
                    request, f'{product.name} - quantity updated.')
            else:
                bag.pop(item_id)
                messages.success(
                    request, f'{product.name} - removed from bag.')

    else:
        print("quantity out of range!")
        messages.error(request, 'Quantity out of range!')

    request.session['bag'] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    # Remove product from the shopping bag

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
            # products without size
            if size == item_id:
                size = None
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['product_data'][size]
            messages.success(
                request, f'{product.name} - {size.split("_")[0]} - removed from bag.')
            if not bag[item_id]['product_data']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)
            messages.success(
                request, f'{product.name} - removed from bag.')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}.')
        return HttpResponse(status=500)
