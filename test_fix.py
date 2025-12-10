import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nerdhub.settings')
django.setup()

from django.contrib.auth.models import User
from nucleo.models import Produto, Carrinho, ItemCarrinho, Estoque

def test_cart_with_and_without_stock():
    # Get the admin user
    user = User.objects.get(username='admin')
    print(f"Using user: {user.username}")
    
    # Get the first product
    produto = Produto.objects.first()
    print(f"Using product: {produto.nome}")
    
    # Check if the product has stock control
    try:
        estoque = produto.estoque
        print(f"Product has stock control: {estoque.quantidade} units")
    except:
        print("Product has no stock control")
    
    # Create or get cart for user
    carrinho, created = Carrinho.objects.get_or_create(usuario=user)
    print(f"Cart created: {created}")
    
    # Clear the cart first
    carrinho.itens.all().delete()
    
    # Add item to cart (should work now even without stock)
    item, created = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho,
        produto=produto,
        defaults={'quantidade': 1}
    )
    
    if not created:
        item.quantidade += 1
        item.save()
        print(f"Updated item quantity to: {item.quantidade}")
    else:
        print(f"Added new item with quantity: {item.quantidade}")
    
    # List items in cart
    itens = carrinho.itens.all()
    print(f"\nItems in cart:")
    total = 0
    for item in itens:
        item_total = item.produto.preco * item.quantidade
        total += item_total
        print(f"- {item.produto.nome}: {item.quantidade} x R${item.produto.preco} = R${item_total}")
    
    print(f"\nTotal cart value: R${total}")
    
    # Test adding more items to test stock validation
    print("\n--- Testing stock validation ---")
    original_quantity = item.quantidade
    
    # Try to add more items (up to 10 times)
    for i in range(10):
        try:
            item.quantidade += 1
            item.save()
            print(f"Increased quantity to: {item.quantidade}")
        except Exception as e:
            print(f"Failed to increase quantity: {e}")
            break
    
    print(f"Final quantity: {item.quantidade}")

if __name__ == '__main__':
    test_cart_with_and_without_stock()