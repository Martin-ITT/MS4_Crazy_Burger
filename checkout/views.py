from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'The shopping bag is empty!')

        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JeRUxGMghRRIS16cssxqfPfn8P6ZtIunBpuHvUcKi0nDzElLf1rz1lBvczgE5dWkCWWhObJ1WHMNwCco0jJ743n00ggdtcCDG',
        'client_secret': 'some_secret',
    }

    return render(request, template, context)
