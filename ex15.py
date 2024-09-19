import os
os.system('cls')

lista_compras = []
total_geral = 0
nome_produto = ""

print("Digite 'fim' para encerrar as entradas.")

while nome_produto.lower() != "fim":
    nome_produto = input("Nome do produto: ")
    
    if nome_produto.lower() != "fim":
        quantidade = input("Quantidade: ")
        while not quantidade.isdigit():
            print("Quantidade inválida! Insira um número inteiro.")
            quantidade = input("Quantidade: ")
        quantidade = int(quantidade)

        preco_unitario = input("Preço unitário: ")
        while not preco_unitario.replace('.', '', 1).isdigit():
            print("Preço inválido! Insira um número válido.")
            preco_unitario = input("Preço unitário: ")
        preco_unitario = float(preco_unitario)

        lista_compras.append((nome_produto, quantidade, preco_unitario))

print("\nLista de Compras:")
print(f"{'Produto':<20}{'Quantidade':<15}{'Preço Unitário':<20}{'Preço Total':<20}")
for produto, quantidade, preco_unitario in lista_compras:
    preco_total = quantidade * preco_unitario
    total_geral += preco_total
    print(f"{produto:<20}{quantidade:<15}{preco_unitario:<20.2f}{preco_total:<20.2f}")

print(f"\nValor total das compras: R$ {total_geral:.2f}")