from django.urls import path
from BBAECAPP import views
from BBAEC import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('banquets',views.banquets),
    path('offers',views.offers),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.ulogout),
    path('menuview',views.menuview),
    path('banqpreview/<bid>',views.banqpreview),
    path('cart',views.cart),
    path('bbanqcart/<bid>',views.bbanqcart),
    path('mmenucart/<mid>',views.mmenucart),
    path('mremove/<uid>',views.mremove),
    path('bremove/<uid>',views.bremove),
    path('cmremove/<uid>',views.cmremove),
    path('updateqty/<qv>/<mid>',views.updateqty),
    path('placeorder',views.placeorder),
    path('bkplaceorder',views.bkplaceorder),
    path('makepayment',views.makepayment),
    path('bkmakepayment',views.bkmakepayment),
    path('bkfinalplaceorder',views.bkfinalplaceorder),  
    path('mportal',views.mportal),
    path('custbooking',views.custbooking),
    path('confirmm/<mid>',views.confirmm),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)