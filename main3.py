
limite = int(input("Digite um número: "))

print("Números pares de 0 até", limite, ":")
for i in range(0, limite + 1):
    if i % 2 == 0:
        print(i, end=" ")
