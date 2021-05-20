"""Un vendedor recibe un sueldo base, mas un 10% extra por comisión de
sus ventas, el vendedor desea saber cuanto dinero obtendrá por
concepto de comisiones por las tres ventas que realiza en el mes y el
total que recibirá en el mes tomando en cuenta su sueldo base y
comisiones."""

# Variables y constantes
PORCENTAJE_COMISION = 0.10

# Entradas de información
salario_base = float(input("Ingrese por favor su salario base: "))
ventas = float(input("Ingrese el total de las ventas: "))

# Proceso
comision =  ventas * PORCENTAJE_COMISION
salario_con_comisiones = salario_base + comision

#Salidas
print(f"Las comisiones de este mes son: {comision}")
print(f"El salario que recibirá este mes es: {salario_con_comisiones}")