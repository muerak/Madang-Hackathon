from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from member.models import Member
from .models import Reservation
from LimitList.models import LimitProduct  # Import the LimitProduct model

def reservation(request):
    members = Member.objects.all()
    context = {
        'members': members,
    }

    reservation_items = Reservation.objects.all()

    total_price = sum(item.reservation_product.limit_discount_price * item.quantity for item in reservation_items)

    # Calculate total price for each reservation item and add it to the context
    for item in reservation_items:
        item.sum_price = item.reservation_product.limit_discount_price * item.quantity


    return render(request, 'reservation/reservation.html', {
        'reservation_items': reservation_items,
        'total_price': total_price,
    })

def add_reservation(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))

        selected_product = get_object_or_404(LimitProduct, id=product_id)

        # Calculate the total quantity of reservations for the selected product
        total_reserved_quantity = Reservation.objects.filter(reservation_product=selected_product).aggregate(Sum('quantity'))['quantity__sum']
        if total_reserved_quantity is None:
            total_reserved_quantity = 0

        if selected_product.limit_stock >= total_reserved_quantity + quantity and total_reserved_quantity + quantity <= 5:
            selected_product.limit_stock -= quantity
            selected_product.save()

            reservation_item, created = Reservation.objects.get_or_create(
                reservation_product=selected_product, defaults={'quantity': quantity}
            )
            if not created:
                reservation_item.quantity += quantity
                reservation_item.save()

            return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect(reverse('LimitList:limit_product_list'))


def logo_click(request):
    phone_last_four = "8180"
    main_url = reverse('member:main', args=[phone_last_four])
    return redirect(main_url)









