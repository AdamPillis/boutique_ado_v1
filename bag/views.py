from django.shortcuts import render, redirect


def view_bag(request):
    """A view that renders the cart content page"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quantity of products specified to the shopping bag"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # storing shopping during their session by creating empty bag object
    bag = request.session.get('bag', {})
    # add or update quantity of product with same id
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    # update bag within session
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
