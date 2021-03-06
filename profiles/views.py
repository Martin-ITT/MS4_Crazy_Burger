from ast import literal_eval
from django.shortcuts import (
    render, get_object_or_404, HttpResponse, redirect, reverse)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        user = request.user
        if form.is_valid():
            # save user_name
            if 'first_name' in request.POST:
                user.first_name = request.POST['first_name']
                user.save()
            if 'last_name' in request.POST:
                user.last_name = request.POST['last_name']
                user.save()
            form.save()
            messages.success(
                request, 'Profile successfully updated!')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
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
        f'This is a past confirmation for order number {order_number[:6]}. '
        'A confirmation email was sent on the order date.'
    ))
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def repeat_order(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    if order.original_bag:
        try:
            bag = literal_eval(order.original_bag)
            request.session['bag'] = bag
            messages.success(request, (
                f'Your shopping bag was updated with items \
                    from order: {order_number[:6]}.'
                ))
        except Exception as e:
            messages.error(
                request, 'Error. There was a problem updating \
                    your bag. Some products might not be available.')
            return HttpResponse(content=e, status=400)
    else:
        messages.error(
                request, 'There was a problem updating your bag. \
                    Some products might not be available.')

    return redirect(reverse("view_bag"))
