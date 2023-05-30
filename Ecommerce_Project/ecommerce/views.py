from django.shortcuts import render
from .models import Product, Category, Brand, Warranty, Seller

def product_category_page(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    warranties = Warranty.objects.all()
    sellers = Seller.objects.all()

    selected_category = request.GET.get('category')
    selected_brand = request.GET.get('brand')
    selected_warranty = request.GET.get('warranty')
    selected_seller = request.GET.get('seller')

    products = Product.objects.all()

    if selected_category:
        products = products.filter(category_id=selected_category)

    if selected_brand:
        products = products.filter(brand_id=selected_brand)

    if selected_warranty:
        products = products.filter(warranty_id=selected_warranty)

    if selected_seller:
        products = products.filter(seller_id=selected_seller)

    context = {
        'categories': categories,
        'brands': brands,
        'warranties': warranties,
        'sellers': sellers,
        'selected_category': int(selected_category) if selected_category else None,
        'selected_brand': int(selected_brand) if selected_brand else None,
        'selected_warranty': int(selected_warranty) if selected_warranty else None,
        'selected_seller': int(selected_seller) if selected_seller else None,
        'products': products,
    }

    return render(request, 'ecommerce/product_category.html', context)