# Un alumno desea saber cual será su calificación final en la materia de Algoritmos
# Dicha calificación se compone de los siguientes porcentajes:
# * 55% del promedio de sus tres calificaciones parciales.
# * 30% de la calificación del examen final.
# * 15% de la calificación de un trabajo final.

parcial_01 = int(input(" Dime la nota del parcial_01 :"))
parcial_02 = int(input(" Dime la nota del parcial_02 :"))
parcial_03 = int(input(" Dime la nota del parcial_03 :"))

examen = int(input(" Dime la nota del examen :"))
trabajo = int(input(" Dime la nota del trabajo :"))

promedio_parciales = (parcial_01 + parcial_02 + parcial_03 )/3
nota_final = (promedio_parciales * 0.55) + (examen * 0.30) + (trabajo * 0.15)

print(" Nota final :" , nota_final)