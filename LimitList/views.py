from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import LimitProduct
from reservation.models import Reservation

def limit_product_list(request):
    limit_products = LimitProduct.objects.all()
    for product in limit_products:
        total_reserved_quantity = Reservation.objects.filter(reservation_product=product).aggregate(Sum('quantity'))['quantity__sum']
        product.total_reserved_quantity = total_reserved_quantity if total_reserved_quantity else 0
    return render(request, 'LimitList/limit.html', {'limit_products': limit_products})


def reserve_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(LimitProduct, id=product_id)
        selected_quantity = int(request.POST.get('quantity'))

        if selected_quantity <= product.limit_stock:
            product.limit_stock -= selected_quantity
            product.save()

            return JsonResponse({'status': 'success', 'remaining_stock': product.limit_stock})
        else:
            return JsonResponse({'status': 'error', 'message': 'Not enough stock available.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def logo_click(request):
    phone_last_four = "8180"
    main_url = reverse('member:main', args=[phone_last_four])
    return redirect(main_url)
