#promys9
trees = [(0,0)]
count = 0

while (0,0) or (0,1) or (0,2) or (1,0) or (1,1) or (2,1) in trees:
	for i in range(len(trees)):
		trees.sort()
		treeX = trees[i][0]
		treeY = trees[i][1]
		
		treeNewUp = (treeX,treeY+1)
		treeNewRight = (treeX+1,treeY)
		
		if treeNewUp and treeNewRight not in trees:
			trees.append(treeNewUp)
			trees.append(treeNewRight)
			trees.remove(trees[i])
		
		if count % 2500 == 0:
			print("Reached iteration "+str(count))
		
		if count % 2500 == 0:
			f = open("count"+str(count/2500)+ ".txt", 'w+')
			f.write(str(trees))
			f.close()
		
		count += 1
		
print(trees)
		
