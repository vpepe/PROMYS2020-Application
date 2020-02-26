#promys5

import copy as c

QPnum = 0
QPreq = [2,3,5,7,11,13]
QPupperbound = int(str(input("What is the upper bound for the check? ")))

count, testList = 0, []
for i in range(QPupperbound):
	count += 1
	testList.append(count)

testedList = c.deepcopy(testList)

for i in range(len(testList)):
	numTest = testList[i]
	resultList = []
	print(numTest)
	
	for j in range(len(QPreq)):
		test = QPreq[j]
		num = numTest / test
		resultList.append(num)
	
	for k in range(len(resultList)):
		if resultList[k].is_integer() == True:
			result = testList[i]
			try:
				testedList.remove(result)
			except:
				continue
		else:
			continue

print(testedList)
print(len(testedList))
