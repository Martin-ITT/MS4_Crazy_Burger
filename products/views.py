from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import *

# Create your views here.


def all_products(request):
    """ A view to return the all products including sorting and
    search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    display_categories = None

    """ sorting by"""
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
                
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        """ selecting categories in navbar """

        if 'category' in request.GET:
            category = request.GET['category']
            if ',' in request.GET['category']:
                category = category.split(",")[0]
                print(category)
            category_food = ['burgers', 'pizza', 'loaded_chips', 'salads', 'creoles', 'kebabs', 'wraps', 'baguettes', 'china_town', 'fish', 'sides']
            category_meals_deals = ['kids_meals', 'daily_offers', 'deals', 'meals']
            category_deserts = ['ice_cream', 'crepes', 'milkshakes', 'other_deserts']
            category_other = ['new_products', 'specials', 'drinks', 'extras']
            display_categories = request.GET['category'].split(',')
            
            if category in category_food:
                display_categories = category_food
                display_categories = Category.objects.filter(name__in=display_categories)
            if category in category_meals_deals:
                display_categories = category_meals_deals
                display_categories = Category.objects.filter(name__in=display_categories)
            if category in category_deserts:
                display_categories = category_deserts
                display_categories = Category.objects.filter(name__in=display_categories)
            if category in category_other:
                display_categories = category_other
                display_categories = Category.objects.filter(name__in=display_categories)

        if 'category' in request.GET:
            category = request.GET['category']
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        """ search query """
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'display_categories': display_categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return product details """

    product = get_object_or_404(Product, pk=product_id)
    allergens = product.allergens.all()
    toppings = Topping.objects.all()
    price_meal_extra = product.price_meal - product.price
    price_large_extra = product.price_large - product.price

    context = {
        'product': product,
        'allergens': allergens,
        'toppings': toppings,
        'price_meal_extra': price_meal_extra,
        'price_large_extra': price_large_extra,
    }

    return render(request, 'products/product_detail.html', context)
