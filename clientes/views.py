from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # Filtrando em Django Rest Framework
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome'] # Parametro de ordenação através do nome dos clientes
    search_fields = ['nome', 'cpf'] # Parametro de busca 
    filterset_fields = ['ativo'] # Busca exata, através de um valor booleano, nesse caso é feito por clientes ativos e não ativos