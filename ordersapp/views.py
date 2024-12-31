from django.shortcuts import render,redirect, get_object_or_404
from cartapp.models import Cart
from .forms import OrderCreateForm
from .models import OrderItem,Order
# Create your views here.

def order_create(request):
    cart = None
    cart_id = request.session.get('cart_id')#retrieves the cart_id from the session.

    
    # If a cart_id exists, it tries to fetch the corresponding Cart object. If the cart is empty (cart.item.exists() is False), or doesn’t exist, it redirects to the cart detail page.
    
    if cart_id:
        cart = Cart.objects.get(id=cart_id)

        if not cart or not cart.items.exists():
            return redirect("cartapp:cart_detail")
        
    #if our users want to send the form after filling this
    if request.method=="POST":#request method POST means the user submitted the form.
        form = OrderCreateForm(request.POST)#takes the submitted data and checks if it’s valid using form.is_valid().
        
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
    # If the form is valid, it creates an Order object but does not save it to the database yet (commit=False). This allows you to add additional information before saving.

            for item in cart.items.all():
                OrderItem.objects.create(
                    order = order,
                    product = item.product,
                    price = item.product.price,
                    quantity = item.quantity
                )
    # Loops through all items in the cart and creates an OrderItem for each one, linking it to the newly created order. It saves the product, price, and quantity for each item.

            cart.delete()
            del request.session["cart_id"]     
    # Deletes the cart after processing the order and removes cart_id from the session.

            return redirect("ordersapp:order_confirmation",order.id)#Redirects to an order confirmation page, passing the newly created order's ID.
        
        else:#If the form is not valid, it re-renders the order creation page with any validation errors.
            form = OrderCreateForm()
        return render(request,"ordersapp/order_create.html",{
            "cart":cart, "form":form
        })
    
#Displays a confirmation page for the newly created order.
def order_confirmation(request,order_id):
    order = get_object_or_404(Order,id=order_id)#Fetches the Order using order_id. If it doesn’t exist, raises a 404 error.
    return render(request,"ordersapp/order_confirmation.html",{"order":order})
    #Passes the Order object to the order_confirmation.html template for rendering.