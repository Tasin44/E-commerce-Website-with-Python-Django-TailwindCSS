from django.urls import path
from . import views

app_name = 'storeapp'  # Register the namespace

urlpatterns = [
    #Leave as empty string for base url(home page)
    #path('',views.main,name='main.html'),#main.html is the homepage
    # path('',views.list,name="list.html"),
    # path('list/',views.list,name="list.html"),
    # path('detail/',views.detail,name="detail.html"),

    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name="product_detail"),
]