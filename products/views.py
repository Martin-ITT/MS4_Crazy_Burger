from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.db.models.functions import Lower

from .models import *
from .forms import ProductForm

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
            messages.info(
                    request, f"Showing results for {query}")

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


@login_required
def add_product(request):
    # add product to the store

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, restricted to admin privilege!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, 'Successfully added product!'
            )
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    # edit existing product

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, restricted to admin privilege!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} updated successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please check if form is valid!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    # delete product from store

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, restricted to admin privilege!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted!')

    return redirect(reverse('products'))
