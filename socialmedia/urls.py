from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('instructions',views.instructions,name='instruction'),
	path('index',views.index,name='index'),
	path('login',views.loginuser,name='login'),
    path('signup',views.signup,name='signup'),
    path('profile/<username>', views.profile, name='profile'),
    path('addpost',views.addpost, name = 'addpost'), 
    path('success', views.success, name = 'success'),
    path('logout',views.logout,name='logout'),
    

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)