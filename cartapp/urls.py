from django.urls import path
from .views import cart_add,cart_detail,cart_remove

app_name= "cartapp"
'''
This line sets a namespace for the URLs defined in this module. By using app_name, you can refer to these URLs in templates and other parts of your Django project with a prefix (e.g., cartapp:cart_add). This helps avoid naming conflicts when you have multiple apps with similar URL names.
'''

urlpatterns = [
    path('add/<int:product_id>/',cart_add,name="cart_add"),#path name cart_add,<int:product_id> means we're passing product id
    path("",cart_detail,name="cart_detail"),
    path("remove/<int:product_id>/",cart_remove,name="remove_item")
]

'''
(1)path('add/<int:product_id>/', cart_add, name="cart_add"),

The URL pattern add/<int:product_id>/ specifies that this route will handle requests to /add/ followed by an integer representing the product ID (e.g., 127.0.0.1:8000/add/5/).

URL: /add/<product_id>/
Purpose: Calls the cart_add view when a user adds a product to the cart.
Dynamic Parameter: <int:product_id> captures the product's ID and passes it to the cart_add view.
Name: cart_add — used for referencing this URL.


(2)path("", cart_detail, name="cart_detail"),

URL Pattern: The empty string "" means this route will handle requests to the root URL of this app (e.g., /cart/).
View Function: It calls the cart_detail view function when accessed.
Name: cart_detail — used for referencing this URL.

(3)path("remove/<int:product_id>/", cart_remove, name="remove_item")

URL Pattern: The pattern remove/<int:product_id>/ specifies that this route will handle requests to /remove/ followed by an integer (the product ID) (e.g., /remove/5/).

View Function: It calls the cart_remove view function when accessed.

Name: remove_item — used for referencing this URL.
'''