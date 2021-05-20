"""Un hombre desea saber cuánto dinero se genera por concepto de intereses
sobre la cantidad que tiene en inversión en el banco. El decidirá
reinvertir los intereses siempre y cuando estos excedan a $7000, y en
ese caso desea saber cuánto dinero tendrá finalmente en su cuenta."""

inversion = float(input("Por favor ingrese el capital que desea invertir: "))
porcentaje_interes = float(input("Por favor ingrese el porcentaje de interes: "))
rendimiento = inversion * porcentaje_interes

if rendimiento > 7000:
    capital_final = inversion + rendimiento
    print(f"Este es su capital final {capital_final}")

print(f"Este es su capital {inversion}")