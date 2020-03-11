#promys10
from itertools import permutations
from ast import literal_eval as liteval

n = int(input("Choose an n: "))
trainspeeds = []
outcomes = []
outcomeChars = []

for i in range(n):
	trainspeeds.append(i+1)
	
trainspeedsCombs = list(permutations(trainspeeds, n))

for i in range(len(trainspeedsCombs)):
	permutation = trainspeedsCombs[i]
	permutation = str(permutation)
	outcomes.append(permutation)

outcomesList = str(outcomes)

outcomesList = outcomesList.replace('(','[')
outcomesList = outcomesList.replace(')',']')
outcomesList = outcomesList.replace("'",'')
outcomes = liteval(outcomesList)

for i in range(len(outcomes)):
	outcome = outcomes[i]
	index = -1
	for j in range(len(outcome)-1):
		index += 1
		last = outcome[(-index)-1]
		notLast = outcome[(-index)-2]
		
		if notLast > last:
			outcome.remove(notLast)
			index = -1
			
		if last > notLast:
			continue
			
#print(outcomes)

bottom = len(outcomes)

top = 0
for i in range(bottom):
	outcome = outcomes[i]
	top += len(outcome)

average = top/bottom

print(str(top)+" / "+str(bottom))
