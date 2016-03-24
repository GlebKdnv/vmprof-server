
from django.contrib import admin

from rest_framework import routers
from server.main import MeView, LogViewSet, TokenViewSet
from django.conf.urls import url, include
from django.contrib.staticfiles import views as static

router = routers.DefaultRouter()
router.register(r'log', LogViewSet)
router.register(r'token', TokenViewSet, base_name="token")

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/user/', MeView.as_view()),
    url(r'^$', static.serve, {'path': 'index.html', 'insecure': True}),
]
