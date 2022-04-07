from django.shortcuts import render, redirect


def view_bag(request):
    """A view that renders the cart content page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quantity of products specified to the shopping bag"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # setting default size to none and if product has size, set to that instead
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # storing shopping during their session by creating empty bag object
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        # add or update quantity of product with same id
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
    # update bag within session
    request.session['bag'] = bag
    return redirect(redirect_url)
