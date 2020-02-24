#PROMYS Q2 A/B
import matplotlib.pyplot as graph

sequence = input("Iterate Sequence X or Y? ")

#Iterating Sequence x (2A)
def iterX():
	while True:
		StartingConds = input("Give Xn and Xn-1, real positive numbers, separated by a comma. ")
		userRange = int(input("Give the number of iterations to iterate the sequence by. "))
		StartingConds = str(StartingConds)
		StartingConds = StartingConds.split(',')
		
		if float(StartingConds[0]) > float(StartingConds[1]):
			Xn = StartingConds[0]
			Xn_1 = StartingConds[1]
		elif float(StartingConds[0]) == float(StartingConds[1]):
			print("The chosen numbers are equal. Try again.")
			continue
		else:
			Xn = StartingConds[1]
			Xn_1 = StartingConds[0]
		
		Xn = float(Xn)
		Xn_1 = float(Xn_1)
		
		terms = []
		for i in range(userRange):
			Xn__1 = float(1/(Xn * Xn_1))
			
			if Xn__1 not in terms:
				terms.append(Xn__1)
			
			Xn_1 = Xn
			Xn = Xn__1
		
		print(terms)

		
#Iterating Sequence y (2B)
def iterY():
	while True:
		StartingConds = input("Give Yn and Yn-1, real positive numbers, separated by a comma. ")
		userRange = int(input("Give the number of iterations to iterate the sequence by. "))
		StartingConds = str(StartingConds)
		StartingConds = StartingConds.split(',')
		
		if float(StartingConds[0]) > float(StartingConds[1]):
			Xn = StartingConds[0]
			Xn_1 = StartingConds[1]
		elif float(StartingConds[0]) == float(StartingConds[1]):
			print("The chosen numbers are equal. Try again.")
			continue
		else:
			Xn = StartingConds[1]
			Xn_1 = StartingConds[0]
		
		Xn = float(Xn)
		Xn_1 = float(Xn_1)
		
		terms = []
		termsUnique = []
		
		for i in range(userRange):
			try:
				Xn__1 = float((1-Xn)/(Xn_1)) #Y calculation
				#Xn__1 = float(1/(Xn * Xn_1)) #calculation for the X Sequence, solely used in case of graphs
			except:
				continue
			
			terms.append(Xn__1)
			
			if Xn__1 not in termsUnique:
				termsUnique.append(Xn__1)
			
			Xn_1 = Xn
			Xn = Xn__1
		
		#print(terms)
		termsLen = len(terms)
		xaxis = []
		
		for i in range(termsLen):
			xaxis.append(i)
		
		uniqueTermsLen = len(termsUnique)
		xaxisUnique = []
		
		for j in range(uniqueTermsLen):
			xaxisUnique.append(j)
		
		graph.figure(1)
		graph.plot(xaxis, terms, color="blue", marker='o', markerfacecolor='black', markersize=4)
		graph.title("All terms with " + str(StartingConds))		
		graph.figure(2)
		graph.plot(xaxisUnique, termsUnique, color="blue", marker='o', markerfacecolor='black', markersize=4)
		graph.title("Unique terms with " + str(StartingConds))
		
		graph.show()

if str(sequence).upper() == 'X':
	iterX()
if str(sequence).upper() == 'Y':
	iterY()
