from django.urls import path
from . import views
app_name='ecommerceapp'

urlpatterns = [
    path('',views.allProductCat,name="allProductCat"),
    path('<slug:cat_slug>/',views.allProductCat,name="productByCategory"),
    path('<slug:cat_slug>/<slug:product_slug>/',views.proDetail,name="productCatDetail")
]