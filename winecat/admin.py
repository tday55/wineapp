from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Wine, Tasting

admin.site.register(Wine)
admin.site.register(Tasting)