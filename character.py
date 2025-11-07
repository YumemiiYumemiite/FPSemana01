character1 = ("name", "ataque" , "defesa")
character2 = ("name", "ataque" , "defesa")
character3 = ("name", "ataque" , "defesa")

character1 = ("Raul", 5 , 15)
character2 = ("Maria", 15 , 5)
character3 = ("Carlos", 10 , 10)

String = "[['" + str(character1[0]) + "', (" + str(character1[1]) + ", " + str(character1[2]) + ")], ['" + str(character2[0]) + "', (" + str(character2[1]) + ", " + str(character2[2]) + ")], ['" + str(character3[0]) + "', (" + str(character3[1]) + ", " + str(character3[2]) + ")]]"

print(String)
print("Ataque Maria " + str(character2[1]))
print("Defesa Raul " + str(character1[2]))
