from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view to render the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    # product qty
    quantity = int(request.POST.get('quantity'))
    # identify product with same drink
    drink_quantity = int(request.POST.get('quantity'))
    # identify pizzas with same toppings
    pizza_quantity = int(request.POST.get('quantity'))
    meal_drink = request.POST.get('meal-drink')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    size = None
    pizza_size = None
    toppings = []
    price = None

    print("\n POST request:")
    print(request.POST)
    print("\n item id:")
    print(type(item_id))

    # make it meal selected
    if request.POST.get('is-meal') == 'meal':
        size = request.POST['is-meal']
        price = float(request.POST['id-price-meal'])
    else:
        size = "n/a"
        price = float(request.POST['id-price'])
        meal_drink = 'none'

    # product with size selection
    if 'opt-size' in request.POST:
        size = request.POST['opt-size']

        if size == "small":
            price = float(request.POST['id-price'])

        if size == "medium":
            price = float(request.POST['id-price-medium'])

        if size == "large":
            price = float(request.POST['id-price-large'])

    # product is pizza
    if 'opt-pizza' in request.POST:
        pizza_size = request.POST['opt-pizza']
        if 'opt-topping' in request.POST:
            toppings = request.POST.getlist('opt-topping')
        if pizza_size == "small":
            price = float(request.POST['id-price'])
        if pizza_size == "medium":
            price = float(request.POST['id-price-medium'])
        if pizza_size == "large":
            price = float(request.POST['id-price-large'])

    # add product with size/meal to bag
    if size and not pizza_size:
        # product id already in a bag
        if item_id in list(bag.keys()):
            # size/meal in a bag
            if size in bag[item_id]['items_by_size'].keys():
                # drink not in a bag
                if meal_drink not in bag[item_id]['meal_drink'].keys():
                    bag[item_id]['meal_drink'][meal_drink] = drink_quantity
                    bag[item_id]['items_by_size'][size] += quantity
                    print("\n IF 1/1 - drink not in a bag")
                # drink/size in a bag already
                elif meal_drink in bag[item_id]['meal_drink'].keys():
                    bag[item_id]['meal_drink'][meal_drink] += drink_quantity
                    bag[item_id]['items_by_size'][size] += quantity
                    print("\n ELIF 2/1 - drink/size in a bag already")
                """
                # products with no size option - not needed anymore
                else:
                    bag[item_id]['items_by_size'][size] += quantity
                    print("\n ELSE 3/1 - products with no size option")
                """
            # size/meal not in a bag
            else:
                bag[item_id]['items_by_size'][size] = quantity
                bag[item_id]['price_by_size'][size] = price
                bag[item_id]['meal_drink'][meal_drink] = drink_quantity
                print("\n ELSE 1/2 - size/meal not in a bag")
        # product id added for a first time
        else:
            bag[item_id] = {
                'items_by_size': {size: quantity},
                'price_by_size': {size: price},
                'meal_drink': {meal_drink: drink_quantity},
                'toppings': toppings}
            print("\n Id added for a first time - not pizza")
    
    # add pizzas to bag
    elif pizza_size:
        # id is already in bag
        if item_id in list(bag.keys()):
            # is size already in bag
            if pizza_size in bag[item_id]['items_by_size'].keys():
                # are same toppings on a pizza
                if toppings in bag[item_id]['toppings'].values():
                    print("\n same size same toppings / add quantity")
                    bag[item_id]['pizza_quantity'] += pizza_quantity
                # toppings not same
                else:
                    print("\n same size but not toppings / add pizza to bag")
                    bag[item_id]['items_by_size'][pizza_size] += quantity
                    bag[item_id]['toppings': {pizza_quantity: toppings}]
                    # bag[item_id]['pizza_quantity'] += quantity
            # size not in bag
            else:
                print("\n size not in bag / add pizza")
                bag[item_id] = {
                    'items_by_size': {pizza_size: quantity},
                    'price_by_size': {pizza_size: price},
                    'meal_drink': {meal_drink: drink_quantity},
                    'toppings': {pizza_quantity: toppings},
                    'pizza_quantity': pizza_quantity
                }
        # id not in bag
        else:
            bag[item_id] = {
                    'items_by_size': {pizza_size: quantity},
                    'price_by_size': {pizza_size: price},
                    'meal_drink': {meal_drink: drink_quantity},
                    'toppings': {pizza_quantity: toppings},
                    'pizza_quantity': pizza_quantity
                }
            print("\n Id added for a first time - pizza")

    # add product with no size
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    print("\n")
    request.session['bag'] = bag
    return redirect(redirect_url)
