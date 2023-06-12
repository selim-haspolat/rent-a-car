from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]

# --------------------------------------------------
# Routers
# --------------------------------------------------

from rest_framework.routers import DefaultRouter
from .views import UserView, UserCreateView

router = DefaultRouter()

router.register('create', UserCreateView)
router.register('', UserView)

urlpatterns += router.urls