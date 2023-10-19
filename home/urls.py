
from django.urls import path,include
from home.views import *
from . import views




from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name="home"),
    path('index/',views.home,name="home"),

    path('contact/',views.contact,name="contact"),
    path('loginform/',views.loginform,name="loginform"),
    path('signup/', views.signup, name="signup"),

    path('login/', views.login, name="login"),
    path('logout', views.logout, name="logout"),

]
urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
