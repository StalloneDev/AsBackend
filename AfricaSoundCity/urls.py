
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
   
    path('user/', include('control_user.urls')),
    path('chat/', include('discussion.urls')),
    path('event/', include('evenement.urls')),
    path('form/', include('formation.urls')),
    path('reserv/', include('reservation.urls')),
    path('restau/', include('restauration.urls')),
    path('serve/', include('service.urls')),
    
]
