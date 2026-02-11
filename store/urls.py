from rest_framework.routers import DefaultRouter
from .views import   StoreViewSet
from .products_view import *
from django.urls import path


urlpatterns = [
    path('create/', StoreViewSet.as_view(), name='stores'),
    path('addproducts/', ProductPostView.as_view(), name='products_post'),
    path('catagory/', CatagoryPostView.as_view(), name='catagory_post'),
    path('customerApi/', CustomerDashboardAPI.as_view(), name='customer_dashBaord'),
    path("store/link-product/", LinkProductToStoreAPI.as_view()),
    path('productsByCategory/<str:category>', ProductsByCategory.as_view(), name='Products_by_category'),
#    path('store/products/<int:category_id>/<int:products_id>/<int:store_id>/', 
#      ProductsbyStores.as_view(), 
#      name='products_by_store_details'),
    path('store/products/', ProductsbyStores.as_view(), name='flexible_product_filter'),
    path('store/productdetails/<int:id>', productDetailsView.as_view(), name='productDetailsView'),
    path('store/stores/', GetStoresView.as_view(), name='Stores_list'),
]
