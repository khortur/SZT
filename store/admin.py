from django.contrib import admin
from store.models import Book
from store.models import Shoe

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock', 'year')
admin.site.register(Book, BookAdmin)

class ShoeAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'size', 'price')
admin.site.register(Shoe, ShoeAdmin)
