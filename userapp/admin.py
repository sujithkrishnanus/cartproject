from django.contrib import admin
from .models import Author,Book, cartModel,cartItem

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(cartModel)
admin.site.register(cartItem)