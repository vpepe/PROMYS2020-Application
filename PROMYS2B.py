#Program for iterating sequence Y(n)

step = float(input("Input a step (0.005 rec.) : "))
YnStep = float(input("Input a step for Yn (0.005/0.05 rec.) : "))

import sqlite3

conn = sqlite3.connect('yseq.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE IF NOT EXISTS sequence (ynum real, ynumprevious real, looplen real)''')

YnBase = 2
Yn_1Base = 1
uniqueTerms = []

for r in range(int(input("How many steps of Yn do you want to compute? "))):
	conn = sqlite3.connect('yseq.db')
	curs = conn.cursor()
	
	for b in range(200):
		uniqueTerms = []
		Yn = YnBase
		Yn_1 = Yn_1Base
		
		for i in range(1024):
			try:
				Yn__1 = float((1-Yn)/(Yn_1))
			except:
				continue
			
			if Yn__1 not in uniqueTerms:
				uniqueTerms.append(Yn__1)
				
			Yn_1 = Yn
			Yn = Yn__1
				
		uniqueTermsLength = len(uniqueTerms)
		
		YnBaseSQL = round(YnBase, 3)
		Yn_1BaseSQL = round(Yn_1Base, 3)
		
		curs.execute('''INSERT INTO sequence VALUES (?,?,?)''', (YnBaseSQL,Yn_1BaseSQL,uniqueTermsLength))
		conn.commit()
		
		if (Yn_1Base + step) <= YnBase:
			Yn_1Base += step
		else:
			YnBase += YnStep
			Yn_1Base = 1
		print("Reached Yn: " + str(YnBaseSQL) + " and Yn-1: " + str(Yn_1BaseSQL))
	conn.close()
	print("Set of 200 reached. Restarting \n")

conn.close()
