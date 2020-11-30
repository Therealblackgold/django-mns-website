from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('', views.success, name="success"),
    path('contact.html', views.contact, name="contact"),
   
]
#THIS PATH IS IMPORTANT TO RENDER OUR IMG IN OUR ADMIN
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
