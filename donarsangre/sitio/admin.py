from django.contrib import admin
from sitio.models import Post, Ubication

# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date',)
    list_filter = ('blood_type','expiration_date', 'created_date')
    search_fields = ('body', )
    date_hierarchy = 'created_date'

class AdminUbication(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    list_filter = ('id', 'nombre',)


admin.site.register(Post, AdminPost)
admin.site.register(Ubication, AdminUbication)