#Escriba un programa que siga la siguiente regla de pago:
#- Si gasto hasta $100, pago con dinero en efectivo
#- Si no, si gasto más de $100 pero menos de $300, pago con tarjeta de débito
#- Si no, pago con tarjeta de crédito.
#El programa debe leer el monto del pago y mostrar en pantalla el medio de pago que se
#utilizará.


monto_pago = int(input("¿Cual es el monto del pago?"))

if monto_pago <=100:
    print("Pagar con dinero en efectivo")

if 100 < monto_pago < 300:
    print("Pagar en tarjeta de débito")

if monto_pago > 300:
    print("Pagar con tarjeta de crédito")
    