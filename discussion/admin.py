from django.contrib import admin

from .models import Discussion, Message

# Register your models here.

admin.site.register((Discussion, Message))