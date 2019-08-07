from django.conf.urls import url,include
from django.contrib import admin

from views import CreateProduct,InboxView,ClearView,EditView,SubCategoryView,ProductStockView,ProductStockListView,UpdateView



urlpatterns = [
    
    url(r'/create',CreateProduct.as_view(), name="product_create"),
    url(r'/subcategory', SubCategoryView.as_view(), name="product_sub_category_change"),
    url(r'/stock', ProductStockView.as_view(), name="product_stock"),
    url(r'/list',ProductStockListView.as_view(), name="product_list"),
    url(r'/update/([a-zA-Z\s]+)/$',UpdateView.as_view(), name="update_list"),
    url(r'/updates/edit',EditView.as_view(), name="edit_stock"),
    url(r'/clear/([a-zA-Z\s]+)/$',ClearView.as_view(), name="clear_stock"),
    url(r'/inbox',InboxView.as_view(), name="inbox_usr"),




]