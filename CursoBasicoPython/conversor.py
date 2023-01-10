def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de moendas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: 
"""

opcion = input(menu)

if opcion == "1":
    conversor("colombianos", 3875)
elif opcion == "2":
    conversor("argentinos", 65)
elif opcion == "3":
    conversor("mexicanos", 24)
else:
    print("Ingresa una opcion correcta, por favor")

# #Dolares a pesos
# dolares = float(input("¿Cuántos dolares USD tienes?: "))
# valor_peso = (1 / 3875)
# pesos = dolares / valor_peso
# pesos = str(round (pesos, 2))
# print("Tienes $" + pesos + " pesos")
