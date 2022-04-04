from django.shortcuts import render


def view_bag(request):
    """A view that renders the cart content page"""
    return render(request, 'bag/bag.html')
