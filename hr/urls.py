from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = 'HR Portal Admin'
admin.site.site_title  = 'Leave Management Portal'
admin.site.index_title = 'Welcome Leave Management Portal' 