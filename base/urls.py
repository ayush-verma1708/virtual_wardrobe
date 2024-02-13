from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from base import views
urlpatterns = [
    path('login/',views.loginPage,name= "login"),
    path('logout/',views.logoutUser,name= "logout"),
    path('register/',views.registerUser,name= "register"),
    path('',views.Wardrobe,name='Wardrobe'),
    path('add_items',views.add_clothes,name='add_clothes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

