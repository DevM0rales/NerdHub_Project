from django.contrib.auth.models import User
from nucleo.models import Pedido

print("=== Usuários e Pedidos ===")
users = User.objects.all()
print(f"Total de usuários: {users.count()}")

for u in users:
    pedidos = Pedido.objects.filter(usuario=u)
    print(f"{u.username}: {pedidos.count()} pedidos")