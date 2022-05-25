from django.urls import path 
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
   path('reg',views.register,name='register'),
   path('',views.login,name='login'),
   path('logout',views.logout,name="logout"),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
