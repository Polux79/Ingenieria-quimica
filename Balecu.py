import chemics as cm

#ce = cm.ChemicalEquation('2 HCl + 2 Na -> 2 NaCl + H2')
ce = cm.ChemicalEquation('Cu(NO3)2 + 2 K -> 2 KNO3 + Cu')

ce.balance  # Retorna True para una ecuación balanceada

ce.rct_properties # Presenta un cuadro con las propiedades de los reactivos

ce.prod_properties # Presenta un cuadro con las propiedades de los reactivos

print("Reactivos")
print(ce.rct_properties)

print ("Productos")
print (ce.prod_properties)