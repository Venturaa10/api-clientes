# Validações em Django REST Framework
def cpf_valido(numero_cpf):
    return len(numero_cpf) == 11


def nome_valido(nome):
    # Se não tiver só caracteres alfabeticos, retorna mensangem de erro, se não, retorna 'nome' 
    return nome.isalpha()

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9



# def validate(rg):
#     if len(rg) != 9:
#         raise serializers.ValidationError('O campo deve incluir 9 digitos')
#     return rg
    
# def validate(celular):
#     if len(celular) < 11:
#         raise serializers.ValidationError('O campo deve incluir 11 digitos')
#     return celular