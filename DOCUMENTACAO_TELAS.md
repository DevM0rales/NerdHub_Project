# 📄 Documentação Completa das Telas - NerdHub

Este documento fornece uma visão detalhada de todas as telas HTML e seus respectivos arquivos CSS do projeto NerdHub E-commerce.

---

## 📑 Índice

1. [Base Template](#1-base-template)
2. [Tela Index (Home)](#2-tela-index-home)
3. [Tela de Detalhes do Produto](#3-tela-de-detalhes-do-produto)
4. [Tela de Carrinho](#4-tela-de-carrinho)
5. [Tela de Checkout](#5-tela-de-checkout)
6. [Tela de Perfil do Usuário](#6-tela-de-perfil-do-usuário)
7. [Telas de Autenticação](#7-telas-de-autenticação)
8. [Tela Sobre](#8-tela-sobre)
9. [Tela Suporte](#9-tela-suporte)
10. [Tela Por Marca](#10-tela-por-marca)
11. [Temas e Padrões de Design](#11-temas-e-padrões-de-design)

---

## 1. Base Template

### 📄 Arquivo: `nucleo/templates/nucleo/base.html`
### 🎨 CSS: `nucleo/static/css/style.css`

**Descrição:**
Template base que serve como estrutura principal para todas as páginas do site. Implementa o tema "AvoidNess" com efeito glassmorphism.

**Estrutura Principal:**

```html
<!DOCTYPE html>
<html>
<head>
    - Meta tags (charset, viewport)
    - Título dinâmico ({% block title %})
    - Links para fontes (Poppins)
    - Remix Icons (biblioteca de ícones)
    - CSS base
</head>
<body>
    - Header (Navbar)
    - Conteúdo principal ({% block content %})
    - Footer
</body>
</html>
```

**Componentes do Header:**

1. **Logo/Brand**
   - Texto "NerdHub" com gradiente cyan-teal
   - Link para página inicial

2. **Menu de Navegação**
   ```
   - Home
   - Sobre
   - Suporte
   - Marcas (dropdown com: PlayStation, Xbox, Nintendo, PC)
   ```

3. **Área de Usuário**
   - Se autenticado: Botão "Perfil" e "Sair"
   - Se não autenticado: Botão "Entrar"
   - Ícone de carrinho com contador de itens

**Estilos CSS Principais:**

```css
/* Variáveis de Cor */
--primary: #00d9ff (cyan)
--secondary: #00a8cc (blue)
--dark-bg: #0a0e27 (dark blue)

/* Efeito Glassmorphism */
background: rgba(255, 255, 255, 0.05)
backdrop-filter: blur(10px)
border: 1px solid rgba(255, 255, 255, 0.1)
```

**Funcionalidades:**
- Sistema de mensagens Django (success, error, info)
- Navegação responsiva
- Menu dropdown para marcas
- Contador dinâmico do carrinho

---

## 2. Tela Index (Home)

### 📄 Arquivo: `nucleo/templates/nucleo/index.html`
### 🎨 CSS: `nucleo/static/css/style_index.css`

**Descrição:**
Página principal que exibe o catálogo de produtos em formato de cards com design moderno.

**Estrutura da Página:**

```html
<div class="container">
    <h1>🎮 Catálogo de Produtos</h1>
    
    <div class="produtos-grid">
        {% for produto in produtos %}
            <div class="produto-card">
                <!-- Card do Produto -->
            </div>
        {% endfor %}
    </div>
</div>
```

**Componentes do Card de Produto:**

1. **Imagem do Produto**
   - Dimensões: 100% largura, altura automática
   - Border-radius no topo
   - Object-fit: cover

2. **Informações do Produto**
   ```html
   <div class="produto-info">
       <span class="marca-badge">{{ marca }}</span>
       <h3>{{ nome }}</h3>
       <p class="descricao">{{ descricao }}</p>
       <p class="preco">R$ {{ preco }}</p>
       <a href="detalhes">Ver Detalhes</a>
   </div>
   ```

**Estilos CSS do Card:**

```css
.produto-card {
    background: glassmorphism effect
    border-radius: 15px
    overflow: hidden
    transition: transform 0.3s
    hover: transform translateY(-10px)
    box-shadow: 0 8px 32px rgba(0,0,0,0.3)
}

.marca-badge {
    background: linear-gradient(cyan, teal)
    color: black
    padding: 5px 15px
    border-radius: 20px
    font-size: 0.8rem
}

.preco {
    color: #00d9ff
    font-size: 1.5rem
    font-weight: bold
}
```

**Layout Responsivo:**

- **Desktop:** Grid de 4 colunas
- **Tablet:** Grid de 2 colunas
- **Mobile:** Grid de 1 coluna

**Funcionalidades:**
- Hover effects nos cards
- Link direto para detalhes do produto
- Badge da marca com gradiente
- Sistema de favoritos (JavaScript)

---

## 3. Tela de Detalhes do Produto

### 📄 Arquivo: `nucleo/templates/nucleo/detalhe_produto.html`
### 🎨 CSS: `nucleo/static/css/detalhe_produto.css`

**Descrição:**
Página detalhada de cada produto com galeria de imagens, informações completas, reviews e produtos relacionados.

**Estrutura da Página:**

```html
<div class="produto-detalhes">
    <!-- Seção 1: Galeria e Info Principal -->
    <div class="produto-principal">
        <div class="galeria-imagens">
            <!-- Imagem principal + miniaturas -->
        </div>
        <div class="produto-info-principal">
            <!-- Nome, preço, descrição, botões -->
        </div>
    </div>
    
    <!-- Seção 2: Reviews -->
    <div class="reviews-section">
        <!-- Lista de reviews + formulário -->
    </div>
    
    <!-- Seção 3: Produtos Relacionados -->
    <div class="relacionados-section">
        <!-- Grid de produtos da mesma marca -->
    </div>
</div>
```

**Componentes Principais:**

### 3.1 Galeria de Imagens
```html
<div class="galeria-imagens">
    <div class="imagem-principal">
        <img src="produto.imagem" alt="produto">
    </div>
    <div class="miniaturas">
        <!-- Thumbnails das imagens adicionais -->
    </div>
</div>
```

**Estilos:**
```css
.imagem-principal {
    width: 100%
    max-height: 500px
    border-radius: 15px
    glassmorphism effect
}

.miniaturas {
    display: flex
    gap: 10px
    margin-top: 15px
}
```

### 3.2 Informações do Produto
```html
<div class="produto-info-principal">
    <span class="marca-badge">{{ marca }}</span>
    <h1>{{ nome }}</h1>
    <p class="preco-destaque">R$ {{ preco }}</p>
    <p class="descricao-completa">{{ descricao }}</p>
    
    <div class="acoes-produto">
        <button class="btn-adicionar-carrinho">
            🛒 Adicionar ao Carrinho
        </button>
        <button class="btn-favoritar">
            ❤️ Favoritar
        </button>
    </div>
</div>
```

**Estilos dos Botões:**
```css
.btn-adicionar-carrinho {
    background: linear-gradient(135deg, #00d9ff, #0099cc)
    color: #000
    padding: 15px 30px
    border-radius: 10px
    font-weight: bold
    hover: box-shadow com glow effect
}

.btn-favoritar {
    background: transparent
    border: 2px solid #00d9ff
    color: #00d9ff
    hover: background #00d9ff, color #000
}
```

### 3.3 Seção de Reviews
```html
<div class="reviews-section">
    <h2>⭐ Avaliações</h2>
    
    <!-- Lista de Reviews -->
    <div class="reviews-lista">
        {% for review in reviews %}
        <div class="review-card">
            <div class="review-header">
                <span class="usuario">{{ usuario }}</span>
                <span class="estrelas">⭐ x {{ nota }}</span>
            </div>
            <p class="comentario">{{ comentario }}</p>
            <span class="data">{{ data }}</span>
        </div>
        {% endfor %}
    </div>
    
    <!-- Formulário de Nova Review -->
    <form class="review-form">
        <textarea name="texto"></textarea>
        <select name="nota">
            <option>1 a 5 estrelas</option>
        </select>
        <button type="submit">Enviar Avaliação</button>
    </form>
</div>
```

**Estilos das Reviews:**
```css
.review-card {
    background: rgba(255, 255, 255, 0.05)
    padding: 20px
    border-radius: 12px
    margin-bottom: 15px
    border-left: 3px solid #00d9ff
}

.estrelas {
    color: #ffd700 (gold)
    font-size: 1.1rem
}
```

### 3.4 Produtos Relacionados
- Grid de 4 produtos da mesma marca
- Mesma estrutura de card da página inicial
- Link "Ver Mais" ao final

**Responsividade:**
- **Desktop:** Layout em duas colunas (galeria + info)
- **Tablet:** Layout empilhado, galeria acima
- **Mobile:** Cards de relacionados em coluna única

---

## 4. Tela de Carrinho

### 📄 Arquivo: `nucleo/templates/nucleo/carrinho.html`
### 🎨 CSS: `nucleo/static/css/style_carrinho.css`

**Descrição:**
Tela para visualizar itens no carrinho de compras com resumo do pedido e opção de finalizar.

**Estrutura da Página:**

```html
<div class="carrinho-container">
    <h1>🛒 Meu Carrinho</h1>
    
    {% if itens_com_total %}
    <div class="carrinho-conteudo">
        <!-- Coluna dos Itens -->
        <div class="carrinho-itens">
            <!-- Lista de produtos -->
        </div>
        
        <!-- Coluna do Resumo -->
        <div class="carrinho-resumo">
            <!-- Total e botões -->
        </div>
    </div>
    {% else %}
    <div class="carrinho-vazio">
        <!-- Estado vazio -->
    </div>
    {% endif %}
</div>
```

**Componentes:**

### 4.1 Item do Carrinho
```html
<div class="carrinho-item">
    <div class="item-imagem">
        <img src="{{ produto.imagem }}" alt="produto">
    </div>
    
    <div class="item-detalhes">
        <h3>{{ nome }}</h3>
        <p class="item-preco">R$ {{ preco }}</p>
    </div>
    
    <div class="item-quantidade">
        <span>Quantidade: {{ quantidade }}</span>
    </div>
    
    <div class="item-total">
        <p>R$ {{ total }}</p>
    </div>
    
    <div class="item-acao">
        <a href="remover" class="btn-remover">Remover</a>
    </div>
</div>
```

**Estilos do Item:**
```css
.carrinho-item {
    display: flex
    align-items: center
    gap: 20px
    background: glassmorphism
    padding: 20px
    border-radius: 12px
    margin-bottom: 15px
}

.item-imagem img {
    width: 100px
    height: 100px
    object-fit: cover
    border-radius: 8px
}

.btn-remover {
    background: #ff4444
    color: white
    padding: 8px 16px
    border-radius: 6px
    hover: background #cc0000
}
```

### 4.2 Resumo do Pedido
```html
<div class="carrinho-resumo">
    <div class="resumo-card">
        <h3>Resumo do Pedido</h3>
        
        <div class="resumo-linha">
            <span>Total:</span>
            <span class="resumo-total">R$ {{ total }}</span>
        </div>
        
        <a href="checkout" class="btn-finalizar">
            Finalizar Pedido
        </a>
        
        <a href="index" class="btn-continuar">
            Continuar Comprando
        </a>
    </div>
</div>
```

**Estilos do Resumo:**
```css
.carrinho-resumo {
    position: sticky
    top: 20px
    width: 400px
}

.resumo-total {
    color: #00d9ff
    font-size: 2rem
    font-weight: bold
    text-shadow: 0 0 10px rgba(0,217,255,0.5)
}

.btn-finalizar {
    background: linear-gradient(135deg, #00d9ff, #0099cc)
    width: 100%
    padding: 15px
    text-align: center
    border-radius: 10px
    margin-top: 20px
}
```

### 4.3 Estado Vazio
```html
<div class="carrinho-vazio">
    <p>Seu carrinho está vazio 😢</p>
    <a href="index" class="btn-voltar">
        Voltar para a loja
    </a>
</div>
```

**Layout Responsivo:**
- **Desktop:** Duas colunas (itens + resumo)
- **Mobile:** Coluna única, resumo abaixo dos itens

---

## 5. Tela de Checkout

### 📄 Arquivo: `nucleo/templates/nucleo/checkout.html`
### 🎨 CSS: `nucleo/static/css/style_checkout.css`

**Descrição:**
Página de finalização de pedido onde o cliente preenche dados de entrega e pagamento.

**Estrutura da Página:**

```html
<div class="checkout-container">
    <h1>🛒 Finalizar Pedido</h1>
    
    <form method="post" action="finalizar_pedido">
        <div class="checkout-content">
            <!-- Formulário Principal -->
            <div class="checkout-main">
                <!-- Seção de Endereço -->
                <!-- Seção de Pagamento -->
            </div>
            
            <!-- Resumo Lateral -->
            <div class="checkout-sidebar">
                <!-- Resumo do pedido -->
            </div>
        </div>
    </form>
</div>
```

**Componentes:**

### 5.1 Seção de Endereço de Entrega
```html
<div class="checkout-section">
    <h2>📦 Endereço de Entrega</h2>
    
    <!-- Se tem endereços salvos -->
    <div class="form-group">
        <label>Usar endereço salvo:</label>
        <select id="endereco_salvo">
            <option>Selecione um endereço</option>
            {% for endereco in enderecos_salvos %}
            <option value="{{ endereco.id }}" data-*>
                {{ endereco.label }}
            </option>
            {% endfor %}
        </select>
    </div>
    
    <!-- Campos de Endereço -->
    <div class="form-row">
        <input type="text" name="endereco_destinatario" 
               placeholder="Nome do Destinatário" required>
    </div>
    
    <div class="form-row">
        <input name="endereco_cep" placeholder="CEP">
        <input name="endereco_telefone" placeholder="Telefone">
    </div>
    
    <div class="form-row">
        <input name="endereco_rua" placeholder="Rua">
        <input name="endereco_numero" placeholder="Número">
    </div>
    
    <!-- Mais campos: complemento, bairro, cidade, estado -->
</div>
```

**Estilos do Formulário:**
```css
.checkout-section {
    background: rgba(255, 255, 255, 0.05)
    backdrop-filter: blur(10px)
    border-radius: 15px
    padding: 30px
}

.form-row {
    display: flex
    gap: 15px
    margin-bottom: 15px
}

.form-control {
    background: rgba(255, 255, 255, 0.08)
    border: 1px solid rgba(255, 255, 255, 0.2)
    border-radius: 8px
    padding: 12px 15px
    color: white
    
    focus: {
        border-color: #00d9ff
        box-shadow: 0 0 15px rgba(0,217,255,0.3)
    }
}
```

### 5.2 Seção de Forma de Pagamento
```html
<div class="checkout-section">
    <h2>💳 Forma de Pagamento</h2>
    
    <div class="payment-options">
        <label class="payment-option">
            <input type="radio" name="forma_pagamento" 
                   value="credito" required>
            <div class="payment-card">
                <span class="payment-icon">💳</span>
                <span class="payment-name">Cartão de Crédito</span>
            </div>
        </label>
        
        <!-- Repetir para: débito, PIX, boleto -->
    </div>
</div>
```

**Estilos das Opções de Pagamento:**
```css
.payment-options {
    display: grid
    grid-template-columns: repeat(2, 1fr)
    gap: 15px
}

.payment-card {
    background: rgba(255, 255, 255, 0.05)
    border: 2px solid rgba(255, 255, 255, 0.2)
    border-radius: 12px
    padding: 20px
    text-align: center
    transition: all 0.3s
}

input[type="radio"]:checked + .payment-card {
    background: rgba(0, 217, 255, 0.15)
    border-color: #00d9ff
    box-shadow: 0 0 20px rgba(0,217,255,0.3)
}

.payment-icon {
    font-size: 2.5rem
    display: block
    margin-bottom: 10px
}
```

### 5.3 Resumo do Pedido (Sidebar)
```html
<div class="checkout-sidebar">
    <div class="order-summary">
        <h3>Resumo do Pedido</h3>
        
        <div class="summary-items">
            {% for item in itens_com_total %}
            <div class="summary-item">
                <div class="item-info">
                    <img src="{{ item.produto.imagem }}">
                    <div>
                        <p class="item-name">{{ nome }}</p>
                        <p class="item-qty">Qtd: {{ quantidade }}</p>
                    </div>
                </div>
                <p class="item-price">R$ {{ total }}</p>
            </div>
            {% endfor %}
        </div>
        
        <div class="summary-divider"></div>
        
        <div class="summary-total">
            <span>Total:</span>
            <span class="total-price">R$ {{ total }}</span>
        </div>
        
        <button type="submit" class="btn-finalizar">
            Confirmar Pedido
        </button>
        
        <a href="carrinho" class="btn-voltar">
            Voltar ao Carrinho
        </a>
    </div>
</div>
```

**Estilos do Resumo:**
```css
.checkout-sidebar {
    width: 400px
    position: sticky
    top: 20px
}

.order-summary {
    background: glassmorphism
    padding: 25px
    border-radius: 15px
}

.summary-items {
    max-height: 400px
    overflow-y: auto
}

.summary-divider {
    height: 2px
    background: linear-gradient(90deg, 
        transparent, 
        rgba(0,217,255,0.5), 
        transparent)
    margin: 20px 0
}

.total-price {
    color: #00d9ff
    font-size: 1.5rem
    text-shadow: 0 0 10px rgba(0,217,255,0.5)
}
```

**JavaScript - Auto-preenchimento:**
```javascript
// Preenche formulário ao selecionar endereço salvo
document.getElementById('endereco_salvo').addEventListener('change', function() {
    const option = this.options[this.selectedIndex];
    if (this.value) {
        document.getElementById('endereco_destinatario').value = 
            option.dataset.destinatario;
        // ... outros campos
    }
});
```

**Responsividade:**
- **Desktop:** Duas colunas (formulário + resumo)
- **Tablet/Mobile:** Coluna única

---

## 6. Tela de Perfil do Usuário

### 📄 Arquivo: `nucleo/templates/usuarios/perfil.html`
### 🎨 CSS: `nucleo/static/css/style_perfil_novo.css`

**Descrição:**
Interface completa de gerenciamento de perfil com sistema de abas para organizar diferentes seções.

**Estrutura da Página:**

```html
<div class="container">
    <div class="flex gap-8">
        <!-- Sidebar com Menu -->
        <aside class="sidebar">
            <nav>
                <div class="sidebar-item active" data-tab="perfil">
                    Perfil
                </div>
                <div class="sidebar-item" data-tab="seguranca">
                    Segurança
                </div>
                <!-- Mais itens: endereço, preferências, etc -->
            </nav>
        </aside>
        
        <!-- Conteúdo das Abas -->
        <div class="flex-1">
            <div id="perfil" class="tab-content">
                <!-- Conteúdo Perfil -->
            </div>
            <!-- Mais tabs hidden -->
        </div>
    </div>
</div>
```

**Abas Disponíveis:**

### 6.1 Aba Perfil
```html
<div id="perfil" class="tab-content">
    <!-- Avatar -->
    <div class="avatar-section">
        <div class="avatar-circle">
            <i class="ri-user-line"></i>
        </div>
        <button class="btn-mudar-foto">Mudar Foto</button>
        <button class="btn-remover">Remover</button>
    </div>
    
    <!-- Formulário de Dados -->
    <form method="POST">
        <div class="grid grid-cols-2 gap-6">
            <input name="display_name" placeholder="Nome de Perfil">
            <input name="full_name" placeholder="Nome Completo">
            <input name="email" placeholder="E-mail" readonly>
            <input name="phone" placeholder="Telefone">
            <input name="birth_date" type="date">
            <select name="gender">
                <option>Gênero</option>
            </select>
        </div>
        <button type="submit">Salvar Alterações</button>
    </form>
</div>
```

**Estilos:**
```css
.avatar-circle {
    width: 96px
    height: 96px
    background: linear-gradient(135deg, #00d9ff, #0099cc)
    border-radius: 50%
    display: flex
    align-items: center
    justify-content: center
}

.grid-cols-2 {
    display: grid
    grid-template-columns: repeat(2, 1fr)
    gap: 1.5rem
}

input, select {
    width: 100%
    padding: 12px 16px
    background: rgba(55, 65, 81, 1) /* gray-700 */
    border: 1px solid rgba(75, 85, 99, 1) /* gray-600 */
    border-radius: 8px
    color: white
}
```

### 6.2 Aba Segurança
```html
<div id="seguranca" class="tab-content hidden">
    <!-- Alterar Senha -->
    <div class="section">
        <h3>Alterar Senha</h3>
        <form method="POST">
            <input name="current_password" type="password" 
                   placeholder="Senha Atual">
            <input name="new_password" type="password" 
                   placeholder="Nova Senha">
            <input name="confirm_password" type="password" 
                   placeholder="Confirmar Nova Senha">
            <button type="submit">Alterar Senha</button>
        </form>
    </div>
    
    <!-- Autenticação 2FA -->
    <div class="section">
        <h3>Autenticação em Dois Fatores</h3>
        <div class="toggle-option">
            <div>
                <p>Ativar 2FA</p>
                <p class="subtitle">Adicione segurança extra</p>
            </div>
            <div class="toggle-switch" data-toggle="2fa">
                <div class="toggle-slider"></div>
            </div>
        </div>
    </div>
    
    <!-- Sessões Ativas -->
    <div class="section">
        <h3>Sessões Ativas</h3>
        <div class="session-card">
            <div class="session-icon">💻</div>
            <div class="session-info">
                <p>Chrome - Windows</p>
                <p class="subtitle">São Paulo, Brasil • Ativo agora</p>
            </div>
            <span class="badge-current">Atual</span>
        </div>
        
        <button class="btn-danger">
            Sair de Todos os Dispositivos
        </button>
    </div>
</div>
```

**Estilos do Toggle:**
```css
.toggle-switch {
    width: 50px
    height: 24px
    background: rgba(75, 85, 99, 1)
    border-radius: 12px
    position: relative
    cursor: pointer
}

.toggle-slider {
    width: 20px
    height: 20px
    background: white
    border-radius: 50%
    position: absolute
    top: 2px
    left: 2px
    transition: transform 0.3s
}

.toggle-switch.active .toggle-slider {
    transform: translateX(26px)
    background: #00d9ff
}
```

### 6.3 Aba Endereços
```html
<div id="endereco" class="tab-content hidden">
    <div class="header">
        <h2>Endereços</h2>
        <button onclick="openAddressModal()">
            Adicionar Endereço
        </button>
    </div>
    
    <!-- Grid de Endereços -->
    <div class="grid grid-cols-2 gap-6">
        {% for endereco in enderecos %}
        <div class="address-card">
            <!-- Cabeçalho -->
            <div class="card-header">
                <div class="icon-label">
                    <div class="icon-circle">
                        <i class="ri-map-pin-line"></i>
                    </div>
                    <div>
                        <h3>{{ endereco.label }}</h3>
                        <p>{{ endereco.recipient_name }}</p>
                    </div>
                </div>
                {% if endereco.is_default_shipping %}
                <span class="badge-default">Padrão</span>
                {% endif %}
            </div>
            
            <!-- Dados do Endereço -->
            <div class="address-info">
                <div class="info-line">
                    <i class="ri-road-map-line"></i>
                    <p>{{ rua }}, {{ numero }}</p>
                </div>
                <div class="info-line">
                    <i class="ri-building-line"></i>
                    <p>{{ bairro }}</p>
                </div>
                <div class="info-line">
                    <i class="ri-map-2-line"></i>
                    <p>{{ cidade }} - {{ estado }}</p>
                </div>
                <div class="info-line">
                    <i class="ri-mail-line"></i>
                    <p>CEP: {{ cep }}</p>
                </div>
            </div>
            
            <!-- Ações -->
            <div class="card-actions">
                <button onclick="editAddress(...)">
                    Editar
                </button>
                <form method="POST" action="excluir">
                    <button type="submit">Excluir</button>
                </form>
            </div>
        </div>
        {% endfor %}
    </div>
    
    <!-- Estado Vazio -->
    {% if not enderecos %}
    <div class="empty-state">
        <div class="empty-icon">📍</div>
        <h3>Nenhum endereço cadastrado</h3>
        <p>Adicione um endereço para facilitar suas compras.</p>
        <button onclick="openAddressModal()">
            Adicionar Primeiro Endereço
        </button>
    </div>
    {% endif %}
</div>
```

**Estilos do Card de Endereço:**
```css
.address-card {
    background: rgba(255, 255, 255, 0.05)
    backdrop-filter: blur(10px)
    padding: 24px
    border-radius: 12px
    border: 2px solid transparent
    transition: all 0.3s
}

.address-card:hover {
    border-color: #00d9ff
    background: rgba(255, 255, 255, 0.08)
}

.icon-circle {
    width: 48px
    height: 48px
    background: rgba(0, 217, 255, 0.2)
    border-radius: 12px
    display: flex
    align-items: center
    justify-content: center
}

.icon-circle i {
    color: #00d9ff
    font-size: 1.5rem
}

.badge-default {
    background: rgba(34, 197, 94, 0.2) /* green-500 */
    color: rgb(74, 222, 128) /* green-400 */
    padding: 4px 12px
    border-radius: 9999px
    font-size: 0.75rem
}

.info-line {
    display: flex
    align-items: center
    gap: 8px
    color: rgba(209, 213, 219, 1) /* gray-300 */
    font-size: 0.875rem
}

.info-line i {
    color: rgba(156, 163, 175, 1) /* gray-400 */
}
```

### 6.4 Aba Meus Pedidos
```html
<div id="pedidos" class="tab-content hidden">
    <h2>Meus Pedidos</h2>
    
    {% for pedido in pedidos %}
    <div class="order-card">
        <!-- Cabeçalho do Pedido -->
        <div class="order-header">
            <div>
                <h3>Pedido #{{ pedido.id }}</h3>
                <p>{{ pedido.criado_em|date }}</p>
            </div>
            <div>
                <p class="order-total">R$ {{ pedido.total }}</p>
                <span class="badge-status">
                    {{ pedido.finalizado|yesno:"Finalizado,Em Processamento" }}
                </span>
            </div>
        </div>
        
        <!-- Endereço de Entrega -->
        <div class="order-section">
            <h4>📦 Endereço de Entrega</h4>
            <p><strong>{{ pedido.endereco_destinatario }}</strong></p>
            <p>{{ pedido.endereco_rua }}, {{ pedido.endereco_numero }}</p>
            <p>{{ pedido.endereco_bairro }} - {{ pedido.endereco_cidade }}/{{ pedido.endereco_estado }}</p>
            <p>CEP: {{ pedido.endereco_cep }}</p>
        </div>
        
        <!-- Forma de Pagamento -->
        <div class="order-section">
            <h4>💳 Forma de Pagamento</h4>
            <p>{{ pedido.get_forma_pagamento_display }}</p>
        </div>
        
        <!-- Itens do Pedido -->
        <div class="order-section">
            <h4>Itens do Pedido</h4>
            {% for item in pedido.itens.all %}
            <div class="order-item">
                <img src="{{ item.produto.imagem }}" alt="produto">
                <div>
                    <p>{{ item.produto.nome }}</p>
                    <p>Quantidade: {{ item.quantidade }}</p>
                    <p>Preço unitário: R$ {{ item.preco_unitario }}</p>
                </div>
                <p class="item-price">R$ {{ item.preco_unitario }}</p>
            </div>
            {% endfor %}
        </div>
        
        <!-- Ações -->
        <div class="order-actions">
            <a href="ver-produto">Ver Produto</a>
            <button>Baixar Nota</button>
        </div>
    </div>
    {% endfor %}
</div>
```

**Estilos do Card de Pedido:**
```css
.order-card {
    background: rgba(255, 255, 255, 0.05)
    backdrop-filter: blur(10px)
    padding: 24px
    border-radius: 12px
    margin-bottom: 24px
}

.order-header {
    display: flex
    justify-content: space-between
    align-items: start
    margin-bottom: 16px
}

.order-total {
    color: #00d9ff
    font-size: 1.25rem
    font-weight: bold
}

.badge-status {
    display: inline-block
    margin-top: 8px
    padding: 4px 12px
    border-radius: 9999px
    font-size: 0.75rem
    font-weight: 600
}

.badge-status.finalizado {
    background: rgba(34, 197, 94, 0.5) /* green */
    color: white
}

.badge-status.processamento {
    background: rgba(234, 179, 8, 0.5) /* yellow */
    color: white
}

.order-section {
    border-top: 1px solid rgba(75, 85, 99, 1)
    padding-top: 16px
    margin-top: 16px
}

.order-item {
    display: flex
    align-items: center
    justify-content: space-between
    background: rgba(55, 65, 81, 0.3)
    padding: 12px
    border-radius: 8px
    margin-bottom: 12px
}

.order-item img {
    width: 64px
    height: 64px
    object-fit: cover
    border-radius: 8px
}
```

### 6.5 Aba Produtos (Admin)
Visível apenas para superusuários.

```html
<div id="produtos" class="tab-content hidden">
    <div class="header">
        <h2>Gerenciar Produtos</h2>
        <button onclick="toggleAddProductForm()">
            Adicionar Produto
        </button>
    </div>
    
    <!-- Formulário de Produto (oculto) -->
    <div id="productFormSection" class="hidden">
        <form method="POST" enctype="multipart/form-data">
            <input name="nome" placeholder="Nome do Produto">
            <textarea name="descricao"></textarea>
            <input name="preco" type="number" step="0.01">
            <input name="quantidade_estoque" type="number">
            <select name="marca">
                <option>Selecione uma marca</option>
            </select>
            <select name="categoria">
                <option>Selecione uma categoria</option>
            </select>
            <input name="imagem_principal" type="file" accept="image/*">
            
            <div id="imagePreview" class="hidden">
                <img id="previewImage">
            </div>
            
            <button type="submit">Cadastrar Produto</button>
            <button type="button" onclick="cancelProductForm()">
                Cancelar
            </button>
        </form>
    </div>
    
    <!-- Lista de Produtos -->
    <div class="products-list">
        <!-- Filtros -->
        <div class="filters">
            <input id="searchProducts" placeholder="Buscar produto...">
            <select id="filterMarca">
                <option>Todas as marcas</option>
            </select>
            <select id="filterCategoria">
                <option>Todas as categorias</option>
            </select>
        </div>
        
        <!-- Tabela de Produtos -->
        <table>
            <thead>
                <tr>
                    <th>Imagem</th>
                    <th>Nome</th>
                    <th>Marca</th>
                    <th>Preço</th>
                    <th>Estoque</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                {% for produto in produtos %}
                <tr class="product-row">
                    <td><img src="{{ produto.imagem }}"></td>
                    <td>{{ produto.nome }}</td>
                    <td>{{ produto.marca }}</td>
                    <td>R$ {{ produto.preco }}</td>
                    <td>{{ produto.estoque.quantidade }} un.</td>
                    <td>
                        <a href="visualizar">👁️</a>
                        <a href="editar">✏️</a>
                        <form method="POST" action="remover">
                            <button type="submit">🗑️</button>
                        </form>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
```

**JavaScript - Sistema de Abas:**
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const sidebarItems = document.querySelectorAll('.sidebar-item');
    const tabContents = document.querySelectorAll('.tab-content');
    
    sidebarItems.forEach(item => {
        item.addEventListener('click', function() {
            const tabId = this.getAttribute('data-tab');
            
            // Remover active de todos
            sidebarItems.forEach(si => si.classList.remove('active'));
            tabContents.forEach(tc => tc.classList.add('hidden'));
            
            // Ativar clicado
            this.classList.add('active');
            document.getElementById(tabId).classList.remove('hidden');
        });
    });
});
```

**Estilos da Sidebar:**
```css
.sidebar {
    width: 256px /* 16rem */
    background: rgba(255, 255, 255, 0.05)
    backdrop-filter: blur(10px)
    padding: 24px
    border-radius: 12px
    position: sticky
    top: 96px
}

.sidebar-item {
    padding: 12px 16px
    border-radius: 8px
    cursor: pointer
    transition: all 0.3s
    display: flex
    align-items: center
    gap: 12px
    color: white
}

.sidebar-item:hover {
    background: rgba(255, 255, 255, 0.1)
}

.sidebar-item.active {
    background: linear-gradient(135deg, #00d9ff, #0099cc)
    color: #000
    font-weight: 600
}
```

**Modal de Endereço:**
```css
#addressModal {
    position: fixed
    inset: 0
    background: rgba(0, 0, 0, 0.75)
    backdrop-filter: blur(4px)
    display: flex (quando aberto)
    align-items: center
    justify-content: center
    z-index: 50
}

.modal-content {
    background: rgba(31, 41, 55, 1) /* gray-800 */
    border-radius: 12px
    padding: 32px
    max-width: 672px
    width: 100%
    max-height: 90vh
    overflow-y: auto
}
```

---

## 7. Telas de Autenticação

### 7.1 Tela de Login/Conta

**📄 Arquivo:** `nucleo/templates/usuarios/conta.html`  
**🎨 CSS:** `nucleo/static/css/style_login_cadastro.css`

**Estrutura:**
```html
<div class="auth-container">
    <div class="auth-card">
        <h1>🔐 Entrar na Conta</h1>
        
        <form method="POST">
            {% csrf_token %}
            
            <div class="form-group">
                <label>Usuário</label>
                <input type="text" name="username" required>
            </div>
            
            <div class="form-group">
                <label>Senha</label>
                <input type="password" name="senha" required>
            </div>
            
            <button type="submit" class="btn-login">
                Entrar
            </button>
            
            <p class="link-cadastro">
                Não tem conta? 
                <a href="{% url 'usuario:cadastro' %}">Cadastre-se</a>
            </p>
        </form>
    </div>
</div>
```

### 7.2 Tela de Cadastro

**📄 Arquivo:** `nucleo/templates/usuarios/cadastro.html`  
**🎨 CSS:** `nucleo/static/css/style_login_cadastro.css`

**Estrutura:**
```html
<div class="auth-container">
    <div class="auth-card">
        <h1>📝 Criar Conta</h1>
        
        <form method="POST">
            {% csrf_token %}
            
            <div class="form-group">
                <label>Usuário</label>
                <input type="text" name="username" required>
            </div>
            
            <div class="form-group">
                <label>E-mail</label>
                <input type="email" name="email" required>
            </div>
            
            <div class="form-group">
                <label>Senha</label>
                <input type="password" name="senha" required>
            </div>
            
            <button type="submit" class="btn-cadastro">
                Cadastrar
            </button>
            
            <p class="link-login">
                Já tem conta? 
                <a href="{% url 'usuario:conta' %}">Faça login</a>
            </p>
        </form>
    </div>
</div>
```

**Estilos Compartilhados:**
```css
.auth-container {
    min-height: 100vh
    display: flex
    align-items: center
    justify-content: center
    padding: 20px
}

.auth-card {
    background: rgba(255, 255, 255, 0.05)
    backdrop-filter: blur(10px)
    border: 1px solid rgba(255, 255, 255, 0.1)
    border-radius: 20px
    padding: 40px
    max-width: 450px
    width: 100%
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3)
}

.form-group {
    margin-bottom: 20px
}

.form-group label {
    display: block
    color: white
    margin-bottom: 8px
    font-weight: 500
}

.form-group input {
    width: 100%
    padding: 12px 16px
    background: rgba(255, 255, 255, 0.08)
    border: 1px solid rgba(255, 255, 255, 0.2)
    border-radius: 8px
    color: white
    font-size: 1rem
}

.form-group input:focus {
    outline: none
    border-color: #00d9ff
    box-shadow: 0 0 15px rgba(0, 217, 255, 0.3)
}

.btn-login, .btn-cadastro {
    width: 100%
    padding: 14px
    background: linear-gradient(135deg, #00d9ff, #0099cc)
    color: #000
    border: none
    border-radius: 10px
    font-size: 1.1rem
    font-weight: bold
    cursor: pointer
    transition: all 0.3s
}

.btn-login:hover, .btn-cadastro:hover {
    transform: translateY(-2px)
    box-shadow: 0 6px 20px rgba(0, 217, 255, 0.4)
}

.link-cadastro, .link-login {
    text-align: center
    color: rgba(255, 255, 255, 0.7)
    margin-top: 20px
}

.link-cadastro a, .link-login a {
    color: #00d9ff
    text-decoration: none
    font-weight: 600
}
```

---

## 8. Tela Sobre

### 📄 Arquivo: `nucleo/templates/nucleo/sobre.html`
### 🎨 CSS: `nucleo/static/css/style_sobre.css`

**Descrição:**
Página institucional sobre a NerdHub com informações da empresa, missão e valores.

**Estrutura:**
```html
<div class="sobre-container">
    <!-- Hero Section -->
    <div class="hero-section">
        <h1>🎮 Sobre a NerdHub</h1>
        <p class="subtitle">
            Sua loja geek de confiança desde 2024
        </p>
    </div>
    
    <!-- Nossa História -->
    <div class="section">
        <h2>Nossa História</h2>
        <p>Texto sobre a história da empresa...</p>
    </div>
    
    <!-- Missão, Visão e Valores -->
    <div class="mvv-grid">
        <div class="mvv-card">
            <div class="icon">🎯</div>
            <h3>Missão</h3>
            <p>Proporcionar...</p>
        </div>
        
        <div class="mvv-card">
            <div class="icon">👁️</div>
            <h3>Visão</h3>
            <p>Ser a maior...</p>
        </div>
        
        <div class="mvv-card">
            <div class="icon">💎</div>
            <h3>Valores</h3>
            <ul>
                <li>Qualidade</li>
                <li>Atendimento</li>
                <li>Inovação</li>
            </ul>
        </div>
    </div>
    
    <!-- Time -->
    <div class="section">
        <h2>Nosso Time</h2>
        <div class="team-grid">
            <div class="team-member">
                <div class="avatar">👤</div>
                <h4>Nome</h4>
                <p>Cargo</p>
            </div>
            <!-- Mais membros -->
        </div>
    </div>
</div>
```

**Estilos:**
```css
.hero-section {
    text-align: center
    padding: 80px 20px
    background: linear-gradient(135deg, 
        rgba(0, 217, 255, 0.1), 
        rgba(0, 168, 204, 0.1))
    border-radius: 20px
    margin-bottom: 40px
}

.mvv-grid {
    display: grid
    grid-template-columns: repeat(3, 1fr)
    gap: 30px
    margin: 40px 0
}

.mvv-card {
    background: rgba(255, 255, 255, 0.05)
    backdrop-filter: blur(10px)
    padding: 30px
    border-radius: 15px
    text-align: center
}

.mvv-card .icon {
    font-size: 3rem
    margin-bottom: 15px
}

.team-grid {
    display: grid
    grid-template-columns: repeat(4, 1fr)
    gap: 20px
}

.team-member {
    text-align: center
    padding: 20px
    background: rgba(255, 255, 255, 0.05)
    border-radius: 12px
}

.team-member .avatar {
    width: 80px
    height: 80px
    margin: 0 auto 15px
    background: linear-gradient(135deg, #00d9ff, #0099cc)
    border-radius: 50%
    display: flex
    align-items: center
    justify-content: center
    font-size: 2rem
}
```

---

## 9. Tela Suporte

### 📄 Arquivo: `nucleo/templates/nucleo/suporte.html`
### 🎨 CSS: `nucleo/static/css/style_suporte.css`

**Descrição:**
Página de suporte com FAQ, formulário de contato e canais de atendimento.

**Estrutura:**
```html
<div class="suporte-container">
    <h1>💬 Suporte ao Cliente</h1>
    
    <!-- Canais de Atendimento -->
    <div class="canais-grid">
        <div class="canal-card">
            <i class="ri-mail-line"></i>
            <h3>E-mail</h3>
            <p>suporte@nerdhub.com</p>
            <p class="tempo">Resposta em 24h</p>
        </div>
        
        <div class="canal-card">
            <i class="ri-phone-line"></i>
            <h3>Telefone</h3>
            <p>(11) 1234-5678</p>
            <p class="tempo">Seg-Sex 9h-18h</p>
        </div>
        
        <div class="canal-card">
            <i class="ri-whatsapp-line"></i>
            <h3>WhatsApp</h3>
            <p>(11) 91234-5678</p>
            <p class="tempo">24/7</p>
        </div>
    </div>
    
    <!-- FAQ -->
    <div class="faq-section">
        <h2>❓ Perguntas Frequentes</h2>
        
        <div class="faq-item">
            <div class="faq-question">
                Como faço um pedido?
            </div>
            <div class="faq-answer hidden">
                Adicione produtos ao carrinho...
            </div>
        </div>
        
        <!-- Mais perguntas -->
    </div>
    
    <!-- Formulário de Contato -->
    <div class="contact-form-section">
        <h2>📧 Entre em Contato</h2>
        
        <form method="POST">
            {% csrf_token %}
            
            <div class="form-row">
                <input name="nome" placeholder="Nome" required>
                <input name="email" type="email" 
                       placeholder="E-mail" required>
            </div>
            
            <select name="assunto" required>
                <option value="">Selecione o assunto</option>
                <option>Dúvida sobre produto</option>
                <option>Problema com pedido</option>
                <option>Sugestão</option>
                <option>Outro</option>
            </select>
            
            <textarea name="mensagem" rows="5" 
                      placeholder="Sua mensagem" required>
            </textarea>
            
            <button type="submit">Enviar Mensagem</button>
        </form>
    </div>
</div>
```

**Estilos:**
```css
.canais-grid {
    display: grid
    grid-template-columns: repeat(3, 1fr)
    gap: 20px
    margin: 40px 0
}

.canal-card {
    background: rgba(255, 255, 255, 0.05)
    backdrop-filter: blur(10px)
    padding: 30px
    border-radius: 15px
    text-align: center
    border: 2px solid transparent
    transition: all 0.3s
}

.canal-card:hover {
    border-color: #00d9ff
    transform: translateY(-5px)
}

.canal-card i {
    font-size: 3rem
    color: #00d9ff
    margin-bottom: 15px
}

.tempo {
    color: rgba(255, 255, 255, 0.6)
    font-size: 0.9rem
    margin-top: 10px
}

.faq-item {
    background: rgba(255, 255, 255, 0.05)
    margin-bottom: 10px
    border-radius: 8px
    overflow: hidden
}

.faq-question {
    padding: 20px
    cursor: pointer
    display: flex
    justify-content: space-between
    align-items: center
    color: white
    font-weight: 500
}

.faq-question:hover {
    background: rgba(255, 255, 255, 0.08)
}

.faq-answer {
    padding: 0 20px 20px
    color: rgba(255, 255, 255, 0.8)
}

.faq-answer.hidden {
    display: none
}

.contact-form-section {
    background: rgba(255, 255, 255, 0.05)
    backdrop-filter: blur(10px)
    padding: 40px
    border-radius: 20px
    margin-top: 40px
}

textarea {
    width: 100%
    padding: 12px 16px
    background: rgba(255, 255, 255, 0.08)
    border: 1px solid rgba(255, 255, 255, 0.2)
    border-radius: 8px
    color: white
    resize: vertical
}
```

**JavaScript - FAQ Accordion:**
```javascript
document.querySelectorAll('.faq-question').forEach(question => {
    question.addEventListener('click', function() {
        const answer = this.nextElementSibling;
        answer.classList.toggle('hidden');
    });
});
```

---

## 10. Tela Por Marca

### 📄 Arquivo: `nucleo/templates/nucleo/por_marca.html`
### 🎨 CSS: `nucleo/static/css/style_por_marca.css`

**Descrição:**
Página que lista produtos filtrados por marca específica.

**Estrutura:**
```html
<div class="marca-container">
    <!-- Header da Marca -->
    <div class="marca-header">
        {% if marca.logo %}
        <img src="{{ marca.logo.url }}" alt="{{ marca.nome }}" 
             class="marca-logo">
        {% endif %}
        <h1>{{ marca.nome }}</h1>
        <p class="produto-count">
            {{ produtos.count }} produto{{ produtos.count|pluralize }}
        </p>
    </div>
    
    <!-- Grid de Produtos -->
    <div class="produtos-grid">
        {% for produto in produtos %}
        <div class="produto-card">
            <!-- Mesmo layout do index -->
        </div>
        {% empty %}
        <div class="no-products">
            <p>Nenhum produto encontrado para esta marca.</p>
            <a href="{% url 'nucleo:index' %}">
                Ver todos os produtos
            </a>
        </div>
        {% endfor %}
    </div>
</div>
```

**Estilos:**
```css
.marca-header {
    text-align: center
    padding: 60px 20px
    background: linear-gradient(135deg,
        rgba(0, 217, 255, 0.1),
        rgba(0, 168, 204, 0.05))
    border-radius: 20px
    margin-bottom: 40px
}

.marca-logo {
    max-width: 200px
    height: auto
    margin-bottom: 20px
    filter: drop-shadow(0 0 20px rgba(0, 217, 255, 0.5))
}

.marca-header h1 {
    color: white
    font-size: 3rem
    margin-bottom: 10px
    text-shadow: 0 0 30px rgba(0, 217, 255, 0.5)
}

.produto-count {
    color: rgba(255, 255, 255, 0.7)
    font-size: 1.2rem
}

.no-products {
    grid-column: 1 / -1
    text-align: center
    padding: 60px 20px
}

.no-products p {
    color: rgba(255, 255, 255, 0.6)
    font-size: 1.2rem
    margin-bottom: 20px
}

.no-products a {
    display: inline-block
    background: linear-gradient(135deg, #00d9ff, #0099cc)
    color: #000
    padding: 12px 30px
    border-radius: 8px
    text-decoration: none
    font-weight: 600
}
```

---

## 11. Temas e Padrões de Design

### 11.1 Paleta de Cores

```css
/* Cores Principais */
--primary: #00d9ff        /* Cyan/Teal principal */
--secondary: #00a8cc      /* Blue secundário */
--accent: #0099cc         /* Accent para gradientes */

/* Backgrounds */
--dark-bg: #0a0e27        /* Dark blue principal */
--darker-bg: #050816      /* Dark blue mais escuro */
--card-bg: rgba(255, 255, 255, 0.05)  /* Glassmorphism */

/* Texto */
--text-primary: #ffffff   /* Texto principal */
--text-secondary: rgba(255, 255, 255, 0.7)  /* Texto secundário */
--text-muted: rgba(255, 255, 255, 0.5)      /* Texto desfocado */

/* Estados */
--success: #22c55e        /* Verde sucesso */
--error: #ef4444          /* Vermelho erro */
--warning: #eab308        /* Amarelo aviso */
--info: #3b82f6          /* Azul informação */
```

### 11.2 Efeito Glassmorphism

**CSS Base:**
```css
.glass-effect {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

/* Variações */
.glass-effect-light {
    background: rgba(255, 255, 255, 0.08);
}

.glass-effect-dark {
    background: rgba(0, 0, 0, 0.3);
}
```

### 11.3 Gradientes

```css
/* Gradiente Principal (Cyan to Teal) */
background: linear-gradient(135deg, #00d9ff, #0099cc);

/* Gradiente Alternativo */
background: linear-gradient(90deg, #00d9ff, #00a8cc);

/* Gradiente de Texto */
background: linear-gradient(135deg, #00d9ff, #0099cc);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;

/* Gradiente de Borda */
border-image: linear-gradient(135deg, #00d9ff, #0099cc) 1;
```

### 11.4 Animações e Transições

```css
/* Transição Padrão */
transition: all 0.3s ease;

/* Hover com Transform */
.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 12px 40px rgba(0, 217, 255, 0.4);
}

/* Glow Effect */
.glow {
    box-shadow: 0 0 20px rgba(0, 217, 255, 0.5);
}

/* Pulse Animation */
@keyframes pulse {
    0%, 100% {
        opacity: 1;
    }
    50% {
        opacity: 0.5;
    }
}

.pulse {
    animation: pulse 2s infinite;
}

/* Fade In */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.fade-in {
    animation: fadeIn 0.5s ease;
}
```

### 11.5 Tipografia

```css
/* Fonte Principal */
font-family: 'Poppins', sans-serif;

/* Tamanhos de Texto */
--text-xs: 0.75rem;      /* 12px */
--text-sm: 0.875rem;     /* 14px */
--text-base: 1rem;       /* 16px */
--text-lg: 1.125rem;     /* 18px */
--text-xl: 1.25rem;      /* 20px */
--text-2xl: 1.5rem;      /* 24px */
--text-3xl: 1.875rem;    /* 30px */
--text-4xl: 2.25rem;     /* 36px */

/* Pesos */
--font-light: 300;
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

### 11.6 Espaçamento

```css
/* Sistema de Espaçamento (múltiplos de 4px) */
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-5: 1.25rem;   /* 20px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-10: 2.5rem;   /* 40px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
```

### 11.7 Border Radius

```css
--radius-sm: 6px;
--radius-md: 8px;
--radius-lg: 12px;
--radius-xl: 15px;
--radius-2xl: 20px;
--radius-full: 9999px;  /* Círculo */
```

### 11.8 Breakpoints Responsivos

```css
/* Mobile First Approach */

/* Small devices (phones, 0-639px) */
/* Base styles */

/* Medium devices (tablets, 640px and up) */
@media (min-width: 640px) {
    .container {
        max-width: 640px;
    }
}

/* Large devices (desktops, 1024px and up) */
@media (min-width: 1024px) {
    .container {
        max-width: 1024px;
    }
    
    .produtos-grid {
        grid-template-columns: repeat(4, 1fr);
    }
}

/* Extra large devices (large desktops, 1280px and up) */
@media (min-width: 1280px) {
    .container {
        max-width: 1280px;
    }
}
```

### 11.9 Componentes Reutilizáveis

#### Botões
```css
/* Botão Primário */
.btn-primary {
    background: linear-gradient(135deg, #00d9ff, #0099cc);
    color: #000;
    padding: 12px 24px;
    border-radius: 8px;
    font-weight: 600;
    border: none;
    cursor: pointer;
    transition: all 0.3s;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 217, 255, 0.4);
}

/* Botão Secundário */
.btn-secondary {
    background: transparent;
    color: #00d9ff;
    border: 2px solid #00d9ff;
    padding: 12px 24px;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
}

.btn-secondary:hover {
    background: #00d9ff;
    color: #000;
}

/* Botão de Perigo */
.btn-danger {
    background: #ef4444;
    color: white;
    padding: 12px 24px;
    border-radius: 8px;
    font-weight: 600;
    border: none;
    cursor: pointer;
    transition: all 0.3s;
}

.btn-danger:hover {
    background: #dc2626;
}
```

#### Cards
```css
.card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    padding: 20px;
    transition: all 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
}

.card-header {
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 15px;
    margin-bottom: 15px;
}

.card-body {
    padding: 15px 0;
}

.card-footer {
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 15px;
    margin-top: 15px;
}
```

#### Badges
```css
.badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 600;
}

.badge-primary {
    background: rgba(0, 217, 255, 0.2);
    color: #00d9ff;
}

.badge-success {
    background: rgba(34, 197, 94, 0.2);
    color: #22c55e;
}

.badge-danger {
    background: rgba(239, 68, 68, 0.2);
    color: #ef4444;
}

.badge-warning {
    background: rgba(234, 179, 8, 0.2);
    color: #eab308;
}
```

#### Inputs
```css
.input {
    width: 100%;
    padding: 12px 16px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    color: white;
    font-size: 1rem;
    transition: all 0.3s;
}

.input:focus {
    outline: none;
    border-color: #00d9ff;
    background: rgba(255, 255, 255, 0.12);
    box-shadow: 0 0 15px rgba(0, 217, 255, 0.3);
}

.input::placeholder {
    color: rgba(255, 255, 255, 0.4);
}
```

### 11.10 Ícones

**Biblioteca Utilizada:** Remix Icon (https://remixicon.com/)

```html
<!-- CDN Link no base.html -->
<link href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css" rel="stylesheet">

<!-- Uso dos Ícones -->
<i class="ri-user-line"></i>           <!-- Usuário -->
<i class="ri-shopping-cart-line"></i>  <!-- Carrinho -->
<i class="ri-map-pin-line"></i>        <!-- Localização -->
<i class="ri-heart-line"></i>          <!-- Favorito -->
<i class="ri-star-fill"></i>           <!-- Estrela -->
<i class="ri-close-line"></i>          <!-- Fechar -->
<i class="ri-add-line"></i>            <!-- Adicionar -->
<i class="ri-edit-line"></i>           <!-- Editar -->
<i class="ri-delete-bin-line"></i>     <!-- Deletar -->
```

---

## 12. Funcionalidades JavaScript

### 12.1 Sistema de Mensagens

```javascript
// Mensagens aparecem automaticamente do Django
// Localização: base.html

setTimeout(function() {
    const messages = document.querySelectorAll('.message');
    messages.forEach(msg => {
        msg.style.animation = 'fadeOut 0.5s ease';
        setTimeout(() => msg.remove(), 500);
    });
}, 3000);  // Desaparecem após 3 segundos
```

### 12.2 Contador do Carrinho

```javascript
// Atualiza dinamicamente o número de itens no ícone do carrinho
// Localização: base.html

function updateCartCount() {
    const cartCount = document.querySelector('.cart-count');
    // Número vem do contexto Django
}
```

### 12.3 Menu Dropdown

```javascript
// Dropdown de marcas no header
// Localização: base.html

const dropdown = document.querySelector('.dropdown');
const dropdownMenu = document.querySelector('.dropdown-menu');

dropdown.addEventListener('mouseenter', () => {
    dropdownMenu.classList.add('show');
});

dropdown.addEventListener('mouseleave', () => {
    dropdownMenu.classList.remove('show');
});
```

### 12.4 Sistema de Favoritos

```javascript
// Adiciona/remove favoritos
// Localização: favorites.js

function toggleFavorite(productId) {
    const btn = document.querySelector(`[data-product="${productId}"]`);
    const isFavorited = btn.classList.contains('favorited');
    
    if (isFavorited) {
        btn.classList.remove('favorited');
        btn.innerHTML = '🤍';  // Coração vazio
    } else {
        btn.classList.add('favorited');
        btn.innerHTML = '❤️';  // Coração cheio
    }
    
    // Salvar no localStorage
    saveFavorites(productId, !isFavorited);
}
```

### 12.5 Modal de Endereço

```javascript
// Gerenciamento do modal de endereços
// Localização: perfil.html

function openAddressModal() {
    document.getElementById('addressModal').style.display = 'flex';
    document.getElementById('addressModal').classList.remove('hidden');
}

function closeAddressModal() {
    document.getElementById('addressModal').style.display = 'none';
    document.getElementById('addressModal').classList.add('hidden');
    document.getElementById('addressForm').reset();
}

function editAddress(id, label, recipientName, ...) {
    openAddressModal();
    // Preencher campos do formulário
    document.getElementById('label').value = label;
    // ... outros campos
    document.getElementById('addressForm').action = `/enderecos/atualizar/${id}/`;
}
```

### 12.6 Filtro de Produtos (Admin)

```javascript
// Filtro na tabela de produtos
// Localização: perfil.html

function filterTable() {
    const searchTerm = document.getElementById('searchProducts').value.toLowerCase();
    const marcaFilter = document.getElementById('filterMarca').value;
    const rows = document.querySelectorAll('.product-row');
    
    rows.forEach(row => {
        const nome = row.getAttribute('data-nome');
        const marca = row.getAttribute('data-marca');
        
        const matchesSearch = nome.includes(searchTerm);
        const matchesMarca = !marcaFilter || marca === marcaFilter;
        
        if (matchesSearch && matchesMarca) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}
```

---

## 13. Boas Práticas Implementadas

### 13.1 Acessibilidade

✅ **Contraste de Cores:** Texto branco em fundo escuro (WCAG AA compliant)  
✅ **Labels nos Inputs:** Todos os campos têm labels descritivos  
✅ **Navegação por Teclado:** Todos os elementos interativos são acessíveis via Tab  
✅ **Textos Alternativos:** Todas as imagens têm atributo `alt`  
✅ **Foco Visível:** Estados de focus bem definidos  

### 13.2 Performance

✅ **Lazy Loading:** Imagens carregam sob demanda  
✅ **CSS Minificado:** Em produção  
✅ **Prefetch de Recursos:** Links importantes pré-carregados  
✅ **Otimização de Imagens:** Compressão e formatos modernos  

### 13.3 SEO

✅ **Meta Tags:** Título e descrição em cada página  
✅ **Estrutura Semântica:** Uso correto de H1, H2, etc.  
✅ **URLs Amigáveis:** Nomes descritivos nas rotas  
✅ **Alt Text:** Descrições em todas as imagens  

### 13.4 Segurança

✅ **CSRF Tokens:** Em todos os formulários POST  
✅ **@login_required:** Proteção de rotas privadas  
✅ **Sanitização:** Escape de dados do usuário  
✅ **Permissões:** Verificação de superuser para admin  

---

## 14. Estrutura de Arquivos

```
UC12_Projeto_NerdHub.1-main/
├── nucleo/
│   ├── templates/
│   │   └── nucleo/
│   │       ├── base.html                  # Template base
│   │       ├── index.html                 # Home
│   │       ├── detalhe_produto.html       # Detalhes
│   │       ├── carrinho.html              # Carrinho
│   │       ├── checkout.html              # Checkout
│   │       ├── sobre.html                 # Sobre
│   │       ├── suporte.html               # Suporte
│   │       ├── por_marca.html             # Por Marca
│   │       └── admin_*.html               # Admin views
│   │
│   └── static/
│       ├── css/
│       │   ├── style.css                  # Base CSS
│       │   ├── style_index.css            # Home
│       │   ├── detalhe_produto.css        # Detalhes
│       │   ├── style_carrinho.css         # Carrinho
│       │   ├── style_checkout.css         # Checkout
│       │   ├── style_perfil_novo.css      # Perfil
│       │   ├── style_login_cadastro.css   # Auth
│       │   ├── style_sobre.css            # Sobre
│       │   ├── style_suporte.css          # Suporte
│       │   └── style_por_marca.css        # Por Marca
│       │
│       └── js/
│           └── favorites.js               # Favoritos
│
├── usuarios/
│   └── templates/
│       └── usuarios/
│           ├── perfil.html                # Perfil completo
│           ├── conta.html                 # Login
│           ├── cadastro.html              # Registro
│           └── *.html                     # Outras views
│
└── staticfiles/                           # Arquivos coletados
    ├── admin/                             # Admin do Django
    ├── css/                               # CSS copiados
    └── js/                                # JS copiados
```

---

## 15. Guia de Manutenção

### 15.1 Adicionando uma Nova Tela

1. **Criar template HTML**
   ```bash
   nucleo/templates/nucleo/nova_tela.html
   ```

2. **Criar CSS específico**
   ```bash
   nucleo/static/css/style_nova_tela.css
   ```

3. **Estender o base.html**
   ```html
   {% extends 'nucleo/base.html' %}
   {% block title %}Título{% endblock %}
   {% block content %}
       {% load static %}
       <link rel="stylesheet" href="{% static 'css/style_nova_tela.css' %}">
       <!-- Conteúdo -->
   {% endblock %}
   ```

4. **Adicionar view e URL**

5. **Executar collectstatic**
   ```bash
   python manage.py collectstatic
   ```

### 15.2 Modificando Cores do Tema

1. Editar variáveis CSS em `style.css`:
   ```css
   :root {
       --primary: #sua-cor;
       --secondary: #sua-cor;
   }
   ```

2. Procurar e substituir nos arquivos CSS específicos

3. Testar em todas as telas

### 15.3 Adicionando Novo Componente

1. Criar classe CSS no arquivo apropriado
2. Documentar uso e variações
3. Adicionar exemplo de código HTML
4. Testar responsividade

---

## 16. Troubleshooting

### Problema: Estilos não aparecem
**Solução:**
```bash
python manage.py collectstatic --noinput
```

### Problema: Modal não abre
**Solução:** Verificar se o JavaScript está carregado e se os IDs estão corretos.

### Problema: Layout quebrado no mobile
**Solução:** Verificar media queries e garantir que `viewport` meta tag está presente.

### Problema: Imagens não carregam
**Solução:** Verificar `MEDIA_URL` e `MEDIA_ROOT` no `settings.py`.

---

## 📝 Notas Finais

Esta documentação cobre todas as telas HTML e arquivos CSS do projeto NerdHub. Cada seção detalha:

- 📄 Arquivos envolvidos
- 🎨 Estrutura HTML
- 💅 Estilos CSS aplicados
- ⚡ Funcionalidades JavaScript
- 📱 Comportamento responsivo
- ♿ Considerações de acessibilidade

Para dúvidas ou sugestões, consulte o código-fonte ou entre em contato com a equipe de desenvolvimento.

---

**Última atualização:** Dezembro 2024  
**Versão:** 1.0  
**Autor:** Equipe NerdHub 