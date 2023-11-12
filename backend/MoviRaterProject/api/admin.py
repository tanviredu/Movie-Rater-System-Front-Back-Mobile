from django.contrib import admin
from api.models import Rating,Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
    search_fields = ['title']
    class Meta:
        model = Movie


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id','stars','show_title','show_user']
    search_fields = ['user__username','movie__title']
    
    def show_title(self,obj):
        if obj.movie and obj.movie.title:
            return obj.movie.title
        else:
            return "N/A"
        
    def show_user(self,obj):
        if obj.user and obj.user.username:
            return obj.user.username
        else:
            return "N/A"
    show_title.short_description = "Title"
    show_user.short_description = "Username"
    
    class Meta:
        model = Rating
        
admin.site.register(Movie,MovieAdmin)
admin.site.register(Rating,RatingAdmin)