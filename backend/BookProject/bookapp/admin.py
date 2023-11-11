from django.contrib import admin
from bookapp.models import Book,BookNumber,Character
from django.utils.html import format_html


class BookAdmin(admin.ModelAdmin):
    list_display = ["title","price","display_isbn_10","display_cover"]
    
    def display_cover(self,obj):
        if obj.cover:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.cover.url)
        else:
            return "No Cover"
        
    def display_isbn_10(self,obj):
        if obj.number and obj.number.isbn_10:
            return obj.number.isbn_10
        else:
            return "N/A"
        
    display_cover.short_description = "Cover Preview"
    display_isbn_10.short_description = "ISBN-10"
    class Meta:
        model = Book

class BookNumberAdmin(admin.ModelAdmin):
    list_display = ["id","isbn_10","isbn_13"]
    class Meta:
        model = BookNumber
        

class CharacterAdmin(admin.ModelAdmin):
    list_display = ["id","name","display_book"]
    
    def display_book(self,obj):
        if obj.book and obj.book.title:
            return obj.book.title
        else:
            return "N/A"
    class Meta:
        model = Character

admin.site.register(Book,BookAdmin)
admin.site.register(BookNumber,BookNumberAdmin)
admin.site.register(Character,CharacterAdmin)