from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Product, Basket, BasketItem, Category
from django.views.generic import DetailView, ListView

def home(request):
    return render(request, 'main/home.html')

def basket(request):
    try:
        the_id = request.session['basket_id']
    except:
        the_id = None
    if the_id:
        basket = Basket.objects.get(id=the_id)
        context = {'basket': basket}
    else:
        empty_message = "Your basket is empty, please keep shopping."
        context = {'empty': True, 'empty_message': empty_message}
    
    return render(request, 'main/basket.html', context)

def update_basket(request, slug):
    request.session.set_expiry(120000)
    try:
        qty = request.GET.get('quantity')
        update_qty = True
    except:
        qty = None
        update_qty = False

    try:
        the_id = request.session['basket_id']
    except:
        new_basket = Basket()
        new_basket.save()
        request.session['basket_id'] = new_basket.id 
        the_id = new_basket.id 

    basket = Basket.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    basket_item, created = BasketItem.objects.get_or_create(basket=basket, product=product)
    if created:
        print("yeah")

    if update_qty and qty:
        if int(qty) == 0:
            basket_item.delete()
        else:
            basket_item.quantity = qty
            basket_item.save()  
    else:
        pass

    new_total = 0.00
    for item in basket.basketitem_set.all():
        line_total = float(item.product.price) * item.quantity
        new_total += line_total
    
    request.session['items_total'] = basket.basketitem_set.count()
    basket.total = new_total
    basket.save()
    
    return redirect('basket')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'

#    def get_context_data(self, **kwargs):
#        context =  super(ProductDetailView, self).get_context_data(**kwargs)
#        context['optional_extras'] = OptionalExtras.objects.all()
#        return context


class ProductListView(ListView):
    model = Product
    template_name = 'main/product_list.html'

def about(request):
    return render(request, 'main/about.html')

def products(request):
    return render(request, 'main/products.html')
