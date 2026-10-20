nota1= float(input("Nota del RA1: "))
peso1= int(input("Peso del RA1 (%): "))
nota2= float(input("Nota del RA2: "))
peso2= int(input("Peso del RA2 (%): "))
nota3= float(input("Nota del RA3: "))
peso3= int(input("Peso del RA3 (%): "))
nota4= float(input("Nota del RA4: "))
peso4= int(input("Peso del RA4 (%): "))

aporta1= nota1 * peso1 / 100
aporta2= nota2 * peso2 / 100
aporta3= nota3 * peso3 / 100
aporta4= nota4 * peso4 / 100
nota_final= aporta1 + aporta2 + aporta3 + aporta4
nota_boletin= round(nota_final)

print()
print("==============================================")
print("           NOTA FINAL DEL MÓDULO")
print("==============================================")
print("RA      Nota      Peso      Aporta")
print("----------------------------------------------")
print("RA1     ", nota1, "    ", peso1, "%       ", aporta1)
print("RA2     ", nota2, "    ", peso2, "%       ", aporta2)
print("RA3     ", nota3, "    ", peso3, "%       ", aporta3)
print("RA4     ", nota4, "    ", peso4, "%       ", aporta4)
print("----------------------------------------------")
print("Suma de los pesos:", peso1 + peso2 + peso3 + peso4, "%")
print("Nota final:", nota_final)
print("Nota del boletín:", nota_boletin)
print("¿Aprobado?:", nota_boletin >= 5)
print("==============================================")