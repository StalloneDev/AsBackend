from django.contrib import admin

from .models import Artiste, Evenement, Programme, StreamingEnDirect

# Register your models here.


admin.site.register((Artiste, Evenement, Programme, StreamingEnDirect))