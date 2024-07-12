from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

# No Django Rest, a validação é realizada inteiramente na classe do serializador.
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        # Se a validação não for verdadeira (not validação), retorna mensagem de erro
        if not cpf_valido(data['cpf']):
           raise serializers.ValidationError({'cpf':'O CPF deve incluir 11 digitos.'})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua números neste campo.'})
    
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve incluir 11 digitos.'})

        return data
    
        
    # # Validações em Django REST Framework
    # def validate_cpf(self, cpf):
    #     if len(cpf) != 11:
    #         raise serializers.ValidationError('O CPF deve incluir 11 digitos.')
    #     return cpf

    # def validate_nome(self, nome):
    #     # Se não tiver só caracteres alfabeticos, retorna mensangem de erro, se não, retorna 'nome' 
    #     if not nome.isalpha():
    #         raise serializers.ValidationError('Não inclua números neste campo')
    #     return nome
        
    # def validate_rg(self, rg):
    #     if len(rg) != 9:
    #         raise serializers.ValidationError('O campo deve incluir 9 digitos')
    #     return rg
    
    # def validate_celular(self, celular):
    #     if len(celular) < 11:
    #         raise serializers.ValidationError('O campo deve incluir 11 digitos')
    #     return celular