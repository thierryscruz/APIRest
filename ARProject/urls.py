from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ARApi import views

router = DefaultRouter()
router.register(r'mymodels', views.MyModelViewSet)
router.register(r'pessoa', views.PessoaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
