#Implemente un programa que calcule el salario semanal de un trabajador “X”. Este valor
#se calcula multiplicando las horas semanales trabajadas por el pago por hora. El usuario
#debe ingresar ambos valores a través del teclado.
#Si las horas trabajadas superan las 40, el pago de horas extras se calculará de la
#siguiente forma:
#- Pago doble por hora en caso las horas trabajadas estén en el intervalo [41, 50].
#- Pago triple por hora en caso las horas trabajadas estén en el intervalo [51, 60]
#- Incentivo de S/. 2000 si la cantidad de horas trabajadas es mayor que 60

horas_semanales_trabajadas = int(input("Ingrese las horas semanales trabajadas")) #41
pago_por_hora = int(input("Ingrese el pago por hora")) #60

if horas_semanales_trabajadas <= 40:
    salario_semanal = horas_semanales_trabajadas * pago_por_hora
    print(f"Usted ganará {salario_semanal} soles :)")
    
if 41 <= horas_semanales_trabajadas <= 50:
    horas_extras = horas_semanales_trabajadas - 40
    pago_extra = horas_extras * 2 * pago_por_hora
    horas_sin_extras = horas_semanales_trabajadas - horas_extras
    salario_semanal = (horas_sin_extras * pago_por_hora) + pago_extra
    print(f"Usted ganará {salario_semanal} soles :)")
    
if 51 <= horas_semanales_trabajadas <= 60:
    horas_extras = horas_semanales_trabajadas - 40
    pago_extra = horas_extras * 3 * pago_por_hora
    horas_sin_extras = horas_semanales_trabajadas - horas_extras
    salario_semanal = (horas_sin_extras * pago_por_hora) + pago_extra
    print(f"Usted ganará {salario_semanal} soles :)")
    
if horas_semanales_trabajadas > 60:
    horas_extras = horas_semanales_trabajadas - 40
    horas_sin_extras = horas_semanales_trabajadas - horas_extras
    incentivo = 2000
    salario_semanal = (horas_sin_extras * pago_por_hora) + incentivo
    print(f"Usted ganará {salario_semanal} soles :)")