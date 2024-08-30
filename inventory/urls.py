from django.urls import path
from . import views, endpoints

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:product_id>/update/', views.product_update, name='product_update'),
    path('products/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/<int:supplier_id>/', views.supplier_detail, name='supplier_detail'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/<int:supplier_id>/update/', views.supplier_update, name='supplier_update'),
    path('suppliers/<int:supplier_id>/delete/', views.supplier_delete, name='supplier_delete'),
    # Endpoints para Product
    path('api/products/', endpoints.ProductList.as_view(), name='product_api_list'),
    path('api/products/<int:pk>/', endpoints.ProductDetail.as_view(), name='product_api_detail'),
    # Endpoints para Supplier
    path('api/suppliers/', endpoints.SupplierList.as_view(), name='supplier_api_list'),
    path('api/suppliers/<int:pk>/', endpoints.SupplierDetail.as_view(), name='supplier_api_detail'),
    # Endpoints para PurchaseOrder
    path('api/purchase-orders/', endpoints.PurchaseOrderList.as_view(), name='purchase_order_api_list'),
    path('api/purchase-orders/<int:pk>/', endpoints.PurchaseOrderDetail.as_view(), name='purchase_order_api_detail'),
    # Endpoints para PurchaseOrderItem
    path('api/purchase-order-items/', endpoints.PurchaseOrderItemList.as_view(), name='purchase_order_item_api_list'),
    path('api/purchase-order-items/<int:pk>/', endpoints.PurchaseOrderItemDetail.as_view(), name='purchase_order_item_api_detail'),
]
