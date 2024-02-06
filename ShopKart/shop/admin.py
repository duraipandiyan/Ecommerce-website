from django.contrib import admin
from .models import category
from .models import product

class categoryadmin(admin.ModelAdmin):
  list_display=("name","image","discription")
admin.site.register(category,categoryadmin)
admin.site.register(product)

# Register your models here.
