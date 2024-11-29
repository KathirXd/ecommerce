from django.urls import path
from . import views

urlpatterns = [
    path("", views.index ,name='index'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('products/', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipe_list, name='recipe_list'),
]
 