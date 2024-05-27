from django.urls import path
from BBAECAPP import views
from django.conf.urls.static import static
from BBAEC import settings

urlpatterns = [
    path('',views.Home,name="Home"),
    path('home',views.Home,name="Home"),
    path('preview/<bid>',views.Preview,name="preview"),
    path('login',views.Login,name="login"),
    path('registration',views.Registration,name="registration"),
    path('logout',views.ulogout,name="logout"),
    path('fooddata/<mid>',views.fooddata,name="fooddata"),
    path('addtocart/<bid>',views.addtocart,name="addtocart"),
    # path('placeorder',views.placeorder),
    # path('makepayment',views.makepayment),
    path('remove/<uid>',views.remove),
    path('menuremove/<uid>',views.menuremove),
    path('cart',views.cart,name="cart"),
    path('updateqty/<qv>/<menuid>',views.updateqty),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)