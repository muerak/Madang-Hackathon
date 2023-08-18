from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product

def whole(request):
    products = Product.objects.all()

    context = {
        'filtered_products': products,
        'selected_category': '전체 할인 품목',
    }
    return render(request, 'SaleList/whole.html', context)

def product_list(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'whole.html', context)

def category_filter(request, category):
    if category == 'all':
        all_products = Product.objects.all()
        context = {
            'filtered_products': all_products,
            'selected_category': '전체 보기',
        }
    else:
        filtered_products = Product.objects.filter(category=category)
        context = {
            'filtered_products': filtered_products,
            'selected_category': category,
        }
    return render(request, 'SaleList/whole.html', context)

def logo_click(request):
    phone_last_four = "8180"
    main_url = reverse('member:main', args=[phone_last_four])
    return redirect(main_url)
