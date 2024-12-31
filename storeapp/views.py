from django.shortcuts import render,get_object_or_404
from .models import Category,Product
# Create your views here.

def product_list(request,category_slug=None):
#in order to filter by category ,we should pas in category_slug as a parameter that would help us filter 
    category=None
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    if category_slug:#if category slug is provided 
                category = get_object_or_404(Category, slug=category_slug)
                products = products.filter(category=category)
#this way we're telling django if a category_slug is provided,then we're gonna get a hold of the products that have a foreigh key relationship with category we got a hold of using the category slug

    return render(request, 'list.html', {
        'category':category,
        'products':products,
        'categories':categories,#passing all the available category 
    })
    
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'detail.html', {'product':product})
    #will notice if comes error it is {'product':product} right or wrong 

# def main(request):
#     return render(request,'main.html')

# def list(request):
#     return render(request,'list.html')

# def detail(request):
#     return render(request,'detail.html')