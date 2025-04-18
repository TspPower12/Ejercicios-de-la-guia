#Un banco ofrece distintas tasas de interés a sus clientes dependiendo de los ahorros que
#estos tengan. El banco pagará:
#- El 4% si es que el depósito es de 1000 a más
#- El 5% si es que el depósito llega hasta 5000
#- El 8% si el depósito es de más de 5000
#Desarrolle un programa que calcule cuánto se deberá pagar por interés dependiendo del
#monto depositado

monto_depositado = int(input("Ingrese el monto depositado"))

if monto_depositado >= 1000:
    tasa_interes = (monto_depositado) * 4/100
    monto_a_pagar = monto_depositado + tasa_interes
    print(F"El banco debera pagarle {monto_a_pagar}")

if monto_depositado == 5000:
    tasa_interes = (monto_depositado) * 5/100
    monto_a_pagar = monto_depositado + tasa_interes
    print(f"El banco debera pagarle {monto_a_pagar}")
    
if monto_depositado > 5000:
    tasa_interes = (monto_depositado) * 8/100
    monto_a_pagar = monto_depositado + tasa_interes
    print(f"El banco debera pagarle {monto_a_pagar}")