from rest_framework import viewsets
from .models import Anggota, Buku, Transaksi
from .serializers import AnggotaSerializer, BukuSerializer, TransaksiSerializer, UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class AnggotaViewSet(viewsets.ModelViewSet):
    queryset = Anggota.objects.all()
    serializer_class = AnggotaSerializer

class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer

class TransaksiViewSet(viewsets.ModelViewSet):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer
class BookPopularityView(APIView):
    """
    View untuk mendapatkan data buku terpopuler berdasarkan jumlah peminjaman.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        popularity_data = Buku.objects.annotate(
            borrow_count=Count('transaksi')
        ).order_by('-borrow_count') 

        top_books = popularity_data[:5]
        response_data = []
        for book in top_books:
            response_data.append({
                'judul': book.judul,
                'penulis': book.penulis,
                'borrow_count': book.borrow_count
            })

        return Response(response_data)