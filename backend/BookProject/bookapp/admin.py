from django.contrib import admin
from bookapp.models import Book
from django.utils.html import format_html
class BookAdmin(admin.ModelAdmin):
    list_display = ["title","description","price","display_cover"]
    
    def display_cover(self,obj):
        if obj.cover:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.cover.url)
        else:
            return "No Cover"
        
    display_cover.short_description = "Cover Preview"
    
    class Meta:
        model = Book
        
admin.site.register(Book,BookAdmin)