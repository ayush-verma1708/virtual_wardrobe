from django.urls import path , include
from .views import Wardrobe , add_clothes
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',Wardrobe,name='Wardrobe'),
    path('add_items',add_clothes,name='add_clothes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

