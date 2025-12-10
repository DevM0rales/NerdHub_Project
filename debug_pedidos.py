from django.contrib.auth import get_user_model
from nucleo.models import Pedido

User = get_user_model()

try:
    user = User.objects.get(username='lucas')
    print(f'Usuário encontrado: {user.username}')
    pedidos = Pedido.objects.filter(usuario=user)
    print(f'Pedidos do usuário: {pedidos.count()}')
    
    # Verificar se os pedidos estão corretamente associados
    for pedido in pedidos:
        print(f'- Pedido #{pedido.id}, Total: R${pedido.total}, Usuário ID: {pedido.usuario.id}')
        
except User.DoesNotExist:
    print('Usuário não encontrado')