from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    """
    checkout cart bag containing all products and
    total price including delivery charges
    """
    bag_items = []
    total = 0
    product_count = 0
    # if total is less than threshold, 10% delivery added using decimals
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # total amount from threshold is shown to convince the user to buy more products
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        # else no delivery charges included as over threshold
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

    return context
