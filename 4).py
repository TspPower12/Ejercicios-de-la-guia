#Escriba un programa que solicite el año actual y un valor de año cualquiera. El programa
#debe mostrar cuántos años han pasado desde el año ingresado o cuántos años faltan
#para llegar a ese año. En caso el año ingresado sea igual que el año actual, muestre un
#mensaje indicando ello.

año_actual = int(input("Ingrese el año actual"))
año_cualquiera = int(input("Ingrese un año cualquiera"))

años_transcurridos = ( año_actual - año_cualquiera)
if año_actual > año_cualquiera:
    print(f"Pasaron {años_transcurridos} años")

if año_actual == año_cualquiera:
    print("Ambos años introducidos son iguales")