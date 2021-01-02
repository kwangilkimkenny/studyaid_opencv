from django.conf.urls import url, include
from . import views
from django.urls import path

from django.conf import settings # add
from django.conf.urls.static import static # add

urlpatterns = [
  path('', views.first_view, name='first_view'),
  path('uimage/', views.uimage, name='uimage'), # add
  path('dface/', views.dface, name='dface'), # add
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # add
