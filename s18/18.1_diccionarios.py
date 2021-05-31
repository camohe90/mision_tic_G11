agenda_telefonos = {
    "Alejando" : 123456,
    "Daniel" : 8900,
    "Camilo" : 6789,
    "Pilar" : 45678,
    "Camilo": 21312
}

print(agenda_telefonos)
print(agenda_telefonos["Camilo"])
print(agenda_telefonos["Pilar"])

nuevo_numero = 3016252610
agenda_telefonos["Camilo"] = nuevo_numero
print(agenda_telefonos["Camilo"])

agenda_telefonos.pop("Daniel")
print(agenda_telefonos)

"""
del agenda_telefonos["Daniel"]
print(agenda_telefonos)"""

agenda_telefonos["Bolt"] = 343434
print(agenda_telefonos)

agenda_telefonos["camiLo"] = 343434
print(agenda_telefonos)
