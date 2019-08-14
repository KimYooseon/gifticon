from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

import mainapp.views
import upload.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.views.main.home,name='home'),
    path('home/<int:flag>/<int:id_num>',mainapp.views.main.home,name='home'),
    path('upload/',upload.views.upload_file, name='upload_file'),
    path('mainapp/',include('mainapp.urls')),
    path('accounts/',include('accounts.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)