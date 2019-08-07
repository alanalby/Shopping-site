from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Main_project import settings

from django.contrib.auth import views as auth_views
from customer import views
from views import HomeView,DeleteView,ContactView,MessageView,RegisterationView,AddToCartView,BuyView,ChangePasswordView,AdminHome,MyOrderView,MyProductView1,MyWalletVew,ItemView,MyProductView2,MyProductView3,MyProductView4



urlpatterns = [
    url(r'^home/$',HomeView.as_view() , name="main"),
    url(r'^adminhome/$',AdminHome.as_view() , name="admin_home"),
    url(r'^login/$',views.login , name="customer_login" ),
    url(r'^logout/$',auth_views.logout  ,{"template_name":"index.html"}, name="customer_logout"),
    url(r'^registeration/$', RegisterationView.as_view() , name="customer_regiseraion"),
    url(r'^change/password',ChangePasswordView.as_view() , name="password_change"),
    url(r'^myorder/$',MyOrderView.as_view(), name="my_order"),
    url(r'^item/([a-zA-Z\s]+)/$',ItemView.as_view(), name="my_items"),
    url(r'^delete/([a-zA-Z\s]+)/$',DeleteView.as_view(), name="del_items"),

    url(r'^views1',MyProductView1.as_view(), name="my_product1"),
    url(r'^views2',MyProductView2.as_view(), name="my_product2"),
    url(r'^views3',MyProductView3.as_view(), name="my_product3"),
    url(r'^views4',MyProductView4.as_view(), name="my_product4"),

    url(r'^wallet',MyWalletVew.as_view(), name="mt_wallet"),
    url(r'^buy',BuyView.as_view(), name="buy_view"),
    url(r'^cart/([a-zA-Z\s]+)/$',AddToCartView.as_view(), name="add_to_cart"),
    url(r'^message',MessageView.as_view(), name="message_view"),
    url(r'^contacts/',ContactView.as_view(), name="contact_view"),



    # url(r'^buy/([a-zA-Z\s]+)/$',BuyView.as_view(), name="buy_view")



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()