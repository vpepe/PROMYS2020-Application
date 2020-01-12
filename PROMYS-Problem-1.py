#Program by Valerio Pepe to simplify answers to PROMYS 2020's Application Problem 1.
import math

n = float(input("Enter sequence term (0-15). Know that the sequence breaks down after n(15): "))

sixteen = math.floor((5/3) * (10**n))
fifty = math.floor(5 * (10**n))
thirtythree = math.floor((10/3) * (10**n))

sixteenFinal = (sixteen ** 3)
fiftyFinal = (fifty ** 3)
thirtythreeFinal = (thirtythree ** 3)

total = sixteenFinal + fiftyFinal + thirtythreeFinal

print("Sequence number: "+ str(n) +" Total: " + str(total))
print("Operands: " + str(sixteenFinal) + " + " + str(fiftyFinal) + " + " + str(thirtythreeFinal))
