nomes = input("Digite uma lista de nomes separados por espaço: ").split()

nomes_com_a = [nome for nome in nomes if nome.lower().startswith('a')]
print("Nomes que começam com a letra 'A':", nomes_com_a)
