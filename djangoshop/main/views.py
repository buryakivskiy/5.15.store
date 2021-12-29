from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:  
        products = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        products = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        products = paginator.page(paginator.num_pages) 
    return render(request, 'main/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'page': page})



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'main/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})








def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Support 5.15.store"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          '5.15.storeabob@gmail.com',
                          ['5.15.storeabob@gmail.com'])
                send_mail('5.15.store Support', 'Ваше питання буде скоро розглянуте',
                          '5.15.storeabob@gmail.com',
                          [body['email']])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("main:product_list")

    form = ContactForm()
    return render(request, "main/contact.html", {'form': form})