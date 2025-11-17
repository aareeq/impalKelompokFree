from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnggotaViewSet, BukuViewSet, TransaksiViewSet, RegisterView, BookPopularityView

router = DefaultRouter()
router.register(r'anggota', AnggotaViewSet)
router.register(r'buku', BukuViewSet)
router.register(r'transaksi', TransaksiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('analytics/book-popularity/', BookPopularityView.as_view(), name='book-popularity'),
    path('register/', RegisterView.as_view(), name='register'),
]