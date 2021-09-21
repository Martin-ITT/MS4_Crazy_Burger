from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += Decimal(item_data * product.price)
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': Decimal(item_data),
                'product': product,
                'price': product.price,
                'subtotal': product.price * item_data,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['product_data'].items():
                price = float(item_data['price'][size])
                data = size.split('.')
                size = data[0]
                drink = None
                if size == 'meal':
                    drink = data[2]
                toppings = None
                if data[1] == 'pizza':
                    toppings = data[2].split(',')
                total += Decimal(quantity * price)
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'drink': drink,
                    'toppings': toppings,
                    'price': price,
                    'subtotal': price * quantity,
                })
                """
                if size == 'large':
                    price = item_data['price_by_size']['large']
                    total += Decimal(quantity * price)
                    product_count += quantity
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                        'price': price,
                        'subtotal': price * quantity,
                    })
                if size == 'meal':
                    price = item_data['price_by_size']['meal']
                    meal_drink = item_data['meal_drink']
                    total += Decimal(quantity * price)
                    product_count += quantity
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                        'price': price,
                        'subtotal': price * quantity,
                        'drink': meal_drink,
                    })
                if size == 'n/a':
                    price = item_data['price_by_size']['n/a']
                    total += Decimal(quantity * price)
                    product_count += quantity
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                        'price': price,
                        'subtotal': price * quantity,
                    })
                        """
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_CHARGE
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        if product_count == 0:
            delivery = 0
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    print("\n bag")
    print(bag)
    return context
