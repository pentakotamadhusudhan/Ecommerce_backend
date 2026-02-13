from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import QuerySet
from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .models import *
from .serializers import CatagorySerializer, ProductDashboardSerializer, ProductSerializer, StoreProductSerializer, StoreSerializer
from generic_reponse import *

class ProductPostView(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product
    def post(self, request):
        try:
            # Check if user is a VENDOR (Security check)
            # if request.user.role != "VENDOR":
            #    return error_response(message="Only vendors can post", status_code=403)

            serializer = ProductSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save() # This saves the product to the DB
                return success_response(
                    message="Product posted successfully!",
                    status_code=201,
                    data=serializer.data
                )
            
            return error_response(
                message=serializer.errors,
                status_code=400
            )
            
        except Exception as e:
            return error_response(
                message=str(e),
                status_code=500
            )


    def get(self, request):
        try:
            # Check if user is a VENDOR (Security check)
            # if request.user.role != "VENDOR":
            #    return error_response(message="Only vendors can post", status_code=403)

            query = self.queryset.objects.all()
            serializer = self.serializer_class(query,many=True)
            
            if serializer:
                # serializer.save() # This saves the product to the DB
                return success_response(
                    message="Product posted successfully!",
                    status_code=201,
                    data=serializer.data
                )
            
            return error_response(
                message=serializer.errors,
                status_code=400
            )
            
        except Exception as e:
            return error_response(
                message=str(e),
                status_code=500
            )



class CatagoryPostView(GenericAPIView):
    serializer_class = CatagorySerializer
    queryset = ProductCategory
    def post(self, request):
        try:
            # Check if user is a VENDOR (Security check)
            # if request.user.role != "VENDOR":
            #    return error_response(message="Only vendors can post", status_code=403)

            serializer = CatagorySerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save() # This saves the product to the DB
                return success_response(
                    message="Product posted successfully!",
                    status_code=201,
                    data=serializer.data
                )
            
            return error_response(
                message=serializer.errors,
                status_code=400
            )
            
        except Exception as e:
            return error_response(
                message=str(e),
                status_code=500
            )


    def get(self, request):
        try:
            # Check if user is a VENDOR (Security check)
            # if request.user.role != "VENDOR":
            #    return error_response(message="Only vendors can post", status_code=403)

            query = self.queryset.objects.all()
            serializer = self.serializer_class(query,many=True)
            
            if serializer:
                # serializer.save() # This saves the product to the DB
                return success_response(
                    message="Product posted successfully!",
                    status_code=201,
                    data=serializer.data
                )
            
            return error_response(
                message=serializer.errors,
                status_code=400
            )
            
        except Exception as e:
            return error_response(
                message=str(e),
                status_code=500
            )


class ProductsByCategory(GenericAPIView):
    serializer_class = ProductSerializer
    QuerySet = Product

    def get(self, request, category): # 'category' comes from the URL path
        try:
            # 1. Filter by category_id (or category__category_name) 
            # based on the string passed in the URL
            products = Product.objects.filter(
                category_id=category, 
                is_active=True
            )

            if not products.exists():
                return failed_response(
                    message="No products found for this category",
                    status_code=404
                )

            ser = self.get_serializer(products, many=True)

            return success_response(
                message="Products By Category retrieved successfully",
                status_code=200,
                data=ser.data
            )
            
        except Exception as e:
            print(f"Error: {e}")
            return failed_response(
                message=str(e), # Must convert exception to string
                status_code=400
            )


            
class CustomerDashboardAPI(APIView):
    def get(self, request):
        try:
            dashboard_data = {}
            
            # Use select_related or prefetch_related to avoid 'AttributeError' on missing relationships
            categories = ProductCategory.objects.all()

            for category in categories:
                # filter by category object directly to be safe
                products = Product.objects.filter(
                    category=category, 
                    is_active=True
                ).order_by('-created_at')[:3]
                
                if products.exists():
                    serializer = ProductDashboardSerializer(products, many=True)
                    # Use str(category.name) to ensure the key is a plain string
                    dashboard_data[str(category.category_name)] = serializer.data

            return Response({
                "status": "success",
                "data": dashboard_data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            # FIX: Convert the error 'e' to a string so JSON can serialize it
            return Response({
                "status": "error",
                "message": str(e)  # <--- This 'str()' prevents your exact error
            }, status=status.HTTP_400_BAD_REQUEST)


class LinkProductToStoreAPI(APIView):
    def post(self, request):
        store_id = request.data.get("store_id")
        product_id = request.data.get("product_id")

        if not store_id or not product_id:
            return Response(
                {"error": "store_id and product_id are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            store = Store.objects.get(id=store_id)
            product = Product.objects.get(id=product_id)
        except (Store.DoesNotExist, Product.DoesNotExist):
            return Response(
                {"error": "Store or Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        store_product, created = StoreProduct.objects.get_or_create(
            store=store,
            product=product
        )

        serializer = StoreProductSerializer(store_product)

        if not created:
            return Response(
                {
                    "message": "Product already linked to this store",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "message": "Product linked to store successfully",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class ProductsbyStores(GenericAPIView):
    serializer_class = StoreProductSerializer
    queryset = StoreProduct.objects.all()

    # Note: Removed the extra arguments from the get method
    def get(self, request):
        try:
            # 1. Correct way to get Query Parameters (?category_id=1)
            cat_id = request.query_params.get('category_id')
            prod_id = request.query_params.get('product_id')
            st_id = request.query_params.get('store_id')

            print(f"Filtering for Category: {cat_id}, Product: {prod_id}, Store: {st_id}")

            # 2. Start with all products
            data = StoreProduct.objects.filter(is_active=True)

            # 3. Dynamically apply filters if they are present in the URL
            if cat_id:
                data = data.filter(product__category_id=cat_id)
            if prod_id:
                data = data.filter(product_id=prod_id)
            if st_id:
                data = data.filter(store_id=st_id)

            if not data.exists():
                return failed_response(
                    status_code=404,
                    message="No matching products found."
                )

            serializer = self.get_serializer(data, many=True)

            return success_response(
                status_code=200,
                message="Store product details retrieved",
                data=serializer.data
            )

        except Exception as e:
            print(f"Error occurred: {e}")
            return failed_response(
                status_code=500,
                message=str(e)
            )
        
class productDetailsView(GenericAPIView):
    serializer_class =StoreProductSerializer
    queryset = StoreProduct.objects.all()

    def get(self,request,id):
        da = StoreProduct.objects.get(id=id)
        ser = self.serializer_class(da)
        return success_response(
            status_code=200,
            message="Product details",
            data=ser.data
        )
    

class GetStoresView(GenericAPIView):
    serializer_class =StoreSerializer
    queryset = Store.objects.all()

    def get(self,request):
        da = Store.objects.all()
        ser = self.serializer_class(da,many= True)
        return success_response(
            status_code=200,
            message="Store details",
            data=ser.data
        )