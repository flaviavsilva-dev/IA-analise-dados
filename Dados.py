# #lista
# lista_de_compras = ["Maça", "Detergente", "Arroz"]
# print(lista_de_compras)
# print(lista_de_compras[2])
#adiciona um dado ao fnal da lista
# lista_de_compras.append("feijao")

# lista_de-compras.insert(1,"sabão em po")

# lista_de_compras.remove("Arroz")

# lista_de_compras.pop()
# print(lista_de_compras)

# notas =[10,4,7.5,8,7]
# print(max(notas))
# print(min(notas))
# print(sum(notas))
# print(len(notas))


N1 = float(input("Digite sua primeira nota: "))
N2 = float(input("Digite sua segunda nota: "))
N3 = float(input("Digite sua terceira nota: "))
N4 = float(input("Digite sua quarta nota: "))

lista_de_notas = [N1, N2, N3, N4]
print(lista_de_notas)

print(f"A maior nota foi: {max(lista_de_notas)}")
print(f"A menor nota foi: {min(lista_de_notas)}")
print(f"A soma de todas as notas é igual a: {sum(lista_de_notas)}")

media = sum(lista_de_notas)/len(lista_de_notas)
print(media)

if media >= 6:
    print("aproado")
else:
    print("reprovado")