from django.urls import path

urlpatterns = [
]

# -------------------------------
# Routers
# -------------------------------
from rest_framework.routers import DefaultRouter
from .views import CarView, ReservationView
router = DefaultRouter()
router.register('car', CarView)
router.register('reservation', ReservationView)
urlpatterns += router.urls