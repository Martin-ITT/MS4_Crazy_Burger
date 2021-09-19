from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view to render the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    meal_drink = request.POST.get('meal-drink')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    size = "n/a"
    price = None

    print(request.POST)

    # make it meal selected
    if request.POST.get('is-meal') == 'meal':
        size = request.POST['is-meal']
        price = float(request.POST['id-price-meal'])
    else:
        size = "n/a"
        price = float(request.POST['id-price'])

    # product with size selection
    if request.POST['category-name'] == 'milkshakes':
        size = request.POST['opt-small-large-only']

        if size == "small":
            price = float(request.POST['id-price-small'])

        if size == "medium":
            price = float(request.POST['id-price-medium'])

        if size == "large":
            price = float(request.POST['id-price-large'])

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                if meal_drink != bag[item_id]['meal_drink']:
                    bag[item_id]['meal_drink'][meal_drink] = quantity
                    bag[item_id]['items_by_size'][size] += quantity
                if meal_drink == bag[item_id]['meal_drink']:
                    bag[item_id]['meal_drink'][meal_drink] += quantity
                else:
                    bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
                bag[item_id]['price_by_size'][size] = price
        else:
            bag[item_id] = {'items_by_size': {
                size: quantity}, 'price_by_size': {size: price}, 'meal_drink': {meal_drink: quantity}}

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    print(type(bag[item_id]['meal_drink']))
    print(type(meal_drink))
    request.session['bag'] = bag
    return redirect(redirect_url)
