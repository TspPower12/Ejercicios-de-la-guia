#En una playa de estacionamiento cobran S/. 2.5 por hora o fracción. Diseñe un programa
#que determine cuanto debe pagar un cliente por el estacionamiento de su vehículo,
#conociendo el tiempo de estacionamiento en horas y minutos, siempre que el tiempo sea
#mayor a 1 hora, caso contrario mostrar el mensaje: “No tiene que pagar
#estacionamiento”

horas = int(input("¿Cuantas horas estuvo?"))
minutos = int(input("¿Cuantos minutos estuvo?"))
costo_por_hora = 2.5

if minutos > 1:
    horas = horas + 1

total_a_pagar = horas * costo_por_hora

print(f"Debe pagar por {horas} horas")
print(f"Total a pagar: s/ {total_a_pagar} soles")