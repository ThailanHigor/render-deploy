from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ProdutoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer