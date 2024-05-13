grid = [[14, 21, 12, 23, 34], [24, 19, 22, 32, 15], [22, 11, 34, 16, 27]] # table
supply = [125, 175, 210] # supply
demand = [120, 140, 75, 85, 90] # demand

startR = 0 # start row
startC = 0 # start col
ans = 0
# loop runs until it reaches the bottom right corner
while(startR != len(grid) and startC != len(grid[0])):
	# if demand is greater than supply
	if(supply[startR] <= demand[startC]):
		ans += supply[startR] * grid[startR][startC]
		# subtract the value of supply from the demand
		demand[startC] -= supply[startR]
		startR += 1
	# if supply is greater than demand
	else:
		ans += demand[startC] * grid[startR][startC]
		# subtract the value of demand from the supply
		supply[startR] -= demand[startC]
		startC += 1

print("The initial feasible basic solution is ", ans)
