from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view to render the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    size = None
    price = None

    # make it meal selected
    if request.POST['category-name'] == 'milkshakes':
        size = request.POST['opt-small-large-only']

    if size == "small":
        price = request.POST['id-price-small']
    
    if size == "large":
        price = request.POST['id-price-large']

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
                bag[item_id]['price_by_size'][size] = price
        else:
            bag[item_id] = {'items_by_size': {size: quantity}, 'price_by_size': {size: price}}

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
