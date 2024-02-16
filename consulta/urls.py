from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    #vistas render
    path('view_consultas',views.view_consultas, name='view_consultas'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
