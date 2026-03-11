from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Store, StoreProduct
from .serializers import StoreProductSerializer, StoreSerializer
from django.db.models import Q

class GlobalSearchAPI(GenericAPIView):
    def get(self, request):
        query = request.query_params.get('query', None)
        search_type = request.query_params.get('type', 'all')  # 'product', 'store', or 'all'

        if not query:
            return Response({
                "status": "error", 
                "message": "Search query is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        results = {}

        try:
            # 1. Search Products (we search StoreProduct to show only available/linked products)
            if search_type in ['all', 'product']:
                products = StoreProduct.objects.filter(
                    Q(product__product_name__icontains=query) | 
                    Q(product__description__icontains=query)
                ).filter(is_active=True).distinct()
                
                # Serializing the data
                product_data = StoreProductSerializer(products, many=True).data
                results = product_data

            # 2. Search Stores
            if search_type in ['all', 'store']:
                stores = Store.objects.filter(
                    Q(name__icontains=query) | 
                    Q(description__icontains=query)
                ).filter(is_active=True).distinct()
                
                # Serializing the data
                store_data = StoreSerializer(stores, many=True).data
                results = store_data

            return Response({
                "status": "success",
                "message": "Search results retrieved successfully",
                "data": results
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print("search error : ",e)
            return Response({
                "status": "error",
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)