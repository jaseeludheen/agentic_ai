
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),


    # Login Endpoint
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Logout Endpoint
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('orders/', include('orders.urls')),  # Include the orders app URLs
    path('support/', include('support.urls')),  # Include the support app URLs
    
]   
