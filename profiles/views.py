from django.shortcuts import (
    render, get_object_or_404, HttpResponse, redirect, reverse)
from django.contrib import messages
from ast import literal_eval

# from django.contrib.auth.models import User

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        user = request.user
        # save user_name
        if 'first_name' in request.POST:
            user.first_name = request.POST['first_name']
            user.save()
        if 'last_name' in request.POST:
            user.last_name = request.POST['last_name']
            user.save()
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated!')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))
    print("toto je history order:")
    print(order.original_bag)
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def repeat_order(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, (
        f'Your shopping bag was updated with items from order: {order_number}.'
    ))
    if order.original_bag:
        try:
            bag = literal_eval(order.original_bag)
            print(bag)
            print(type(bag))
            request.session['bag'] = bag

        except Exception as e:
            messages.error(request, 'There was a problem updating your bag. Please try again later.')
            return HttpResponse(content=e, status=400)

    return redirect(reverse("view_bag"))
