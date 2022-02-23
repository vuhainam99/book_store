from django.contrib import admin
from .models import *


admin.site.register(Users)
admin.site.register(Book_info)
admin.site.register(Book_Data)
admin.site.register(User_To_read)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_title', 'book_authors', 'book_price')
admin.site.register(Book, BookAdmin)
admin.site.register(User_rating)
admin.site.register(Order)
admin.site.register(Book_Sales_His)
admin.site.register(Genres)


