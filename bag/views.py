from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    # A view to render the shopping bag page

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    # Add a quantity of the specified product to the shopping bag

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    product_data = None
    price = None

    if 'opt-size' in request.POST:
        size = request.POST['opt-size']
        product_data = size

    if 'is-meal' in request.POST:
        size = request.POST['is-meal']
        drink = request.POST['meal-drink']
        product_data = size + '.' + drink
        if size == 'meal':
            price = request.POST['id-price-meal']
        else:
            price = request.POST['id-price']

    bag = request.session.get('bag', {})
    print("\n request:")
    print(request.POST)

    if product_data:
        if item_id in list(bag.keys()):

            if product_data in bag[item_id]['product_data'].keys():
                bag[item_id]['product_data'][product_data] += quantity
            else:
                bag[item_id]['product_data'][product_data] = quantity
                bag[item_id]['price'][product_data] = price
        else:
            bag[item_id] = {
                'product_data': {product_data: quantity},
                'price': {product_data: price},
                }
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
