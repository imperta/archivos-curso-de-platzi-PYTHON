def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos +  "tienes?:")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")    


menu = """
Bienvenido al conversor de monedas 🤑


1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos mexicanos

Elige una opcion: """

opcion = input(menu)

if opcion == "1" :
    pass
elif opcion == "2":
    pass
elif opcion == "3":
    pass
else:
    print("Ingresa una opcion correcta")

if opcion == "1":
    conversor("Colombianos", 4000)
    
elif opcion == "2":
    conversor("Argentinos", 65)
    
elif opcion == "3":
    conversor("Mexicanos", 20)