from django.shortcuts import render, redirect, get_object_or_404
from .models import Clothes, Product, Category
from .forms import ClothesCreateForm


# def index(request):
#     wear = Clothes.objects.all()
#     return render(request, 'main_page/index.html', {'title': 'Главная страница', 'wear': wear})
#
#
# def about(request):
#     return render(request, "main_page/about.html", {'about': 'О нас'})
#
#
# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = ClothesCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             error = 'Форма неверно заполнена'
#     form = ClothesCreateForm()
#     context = {
#         'form': form
#     }
#     return render(request, "main_page/create.html", context)
#
#
# def cloth_info(request):
#     return render(request, "main_page/cloth_info.html", {'cloth_info': 'Информация об одежде'})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                {'category': category,
                'categories': categories,
                'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})